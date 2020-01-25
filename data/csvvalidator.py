# coding=utf-8
"""
2020.1.26：这份代码来自https://github.com/alimanfoo/csvvalidator
原作者使用的Python2.X, 因此拷贝下来自己修改，也方便打印report时自己定义格式。
感谢原作者： alimanfoo： https://github.com/alimanfoo
"""
"""

This module provides some simple utilities for validating data contained in CSV
files, or other similar data sources.

Note that the `csvvalidator` module is intended to be used in combination with
the standard Python `csv` module. The `csvvalidator` module **will not**
validate the *syntax* of a CSV file. Rather, the `csvvalidator` module can be
used to validate any source of row-oriented data, such as is provided by a
`csv.reader` object.

I.e., if you want to validate data from a CSV file, you have to first construct
a CSV reader using the standard Python `csv` module, specifying the appropriate
dialect, and then pass the CSV reader as the source of data to either the
`CSVValidator.validate` or the `CSVValidator.ivalidate` method.

The `CSVValidator` class is the foundation for all validator objects that are
capable of validating CSV data.

You can use the CSVValidator class to dynamically construct a validator, e.g.::

    import sys
    import csv
    from csvvalidator import *

    field_names = (
                   'study_id',
                   'patient_id',
                   'gender',
                   'age_years',
                   'age_months',
                   'date_inclusion'
                   )

    validator = CSVValidator(field_names)

    # basic header and record length checks
    validator.add_header_check('EX1', 'bad header')
    validator.add_record_length_check('EX2', 'unexpected record length')

    # some simple value checks
    validator.add_value_check('study_id', int,
                              'EX3', 'study id must be an integer')
    validator.add_value_check('patient_id', int,
                              'EX4', 'patient id must be an integer')
    validator.add_value_check('gender', enumeration('M', 'F'),
                              'EX5', 'invalid gender')
    validator.add_value_check('age_years', number_range_inclusive(0, 120, int),
                              'EX6', 'invalid age in years')
    validator.add_value_check('date_inclusion', datetime_string('%Y-%m-%d'),
                              'EX7', 'invalid date')

    # a more complicated record check
    def check_age_variables(r):
        age_years = int(r['age_years'])
        age_months = int(r['age_months'])
        valid = (age_months >= age_years * 12 and
                 age_months % age_years < 12)
        if not valid:
            raise RecordError('EX8', 'invalid age variables')
    validator.add_record_check(check_age_variables)

    # validate the data and write problems to stdout
    data = csv.reader('/path/to/data.csv', delimiter='\t')
    problems = validator.validate(data)
    write_problems(problems, sys.stdout)

For more complex use cases you can also sub-class `CSVValidator` to define
re-usable validator classes for specific data sources.

The source code for this module lives at:

    https://github.com/alimanfoo/csvvalidator

For a complete account of all of the functionality available from this module,
see the example.py and tests.py modules in the source code repository.

"""


import re
from datetime import datetime


UNEXPECTED_EXCEPTION = 0
VALUE_CHECK_FAILED = 1
HEADER_CHECK_FAILED = 2
RECORD_LENGTH_CHECK_FAILED = 3
VALUE_PREDICATE_FALSE = 4
RECORD_CHECK_FAILED = 5
RECORD_PREDICATE_FALSE = 6
UNIQUE_CHECK_FAILED = 7
ASSERT_CHECK_FAILED = 8
FINALLY_ASSERT_CHECK_FAILED = 9

MESSAGES = {
            UNEXPECTED_EXCEPTION: 'Unexpected exception [%s]: %s',
            VALUE_CHECK_FAILED: 'Value check failed.',
            HEADER_CHECK_FAILED: 'Header check failed.',
            RECORD_LENGTH_CHECK_FAILED: 'Record length check failed.',
            RECORD_CHECK_FAILED: 'Record check failed.',
            VALUE_PREDICATE_FALSE: 'Value predicate returned false.',
            RECORD_PREDICATE_FALSE: 'Record predicate returned false.',
            UNIQUE_CHECK_FAILED: 'Unique check failed.',
            ASSERT_CHECK_FAILED: 'Assertion check failed.',
            FINALLY_ASSERT_CHECK_FAILED: 'Final assertion check failed.'
            }


class RecordError(Exception):
    """Exception representing a validation problem in a record."""


    def __init__(self, code=None, message=None, details=None):
        self.code = code
        self.message = message
        self.details = details


    def __str__(self):
        return repr((self.code, self.message, self.details))


    def __repr__(self):
        return repr((self.code, self.message, self.details))


class CSVValidator(object):
    """
    Instances of this class can be configured to run a variety of different
    types of validation check on a CSV-like data source.

    """


    def __init__(self, field_names):
        """
        Instantiate a `CSVValidator`, supplying expected `field_names` as a
        sequence of strings.

        """

        self._field_names = tuple(field_names)
        self._value_checks = []
        self._header_checks = []
        self._record_length_checks = []
        self._value_predicates = []
        self._record_checks = []
        self._record_predicates = []
        self._unique_checks = []
        self._skips = []


    def add_header_check(self,
                         code=HEADER_CHECK_FAILED,
                         message=MESSAGES[HEADER_CHECK_FAILED]):
        """
        Add a header check, i.e., check whether the header record is consistent
        with the expected field names.

        Arguments
        ---------

        `code` - problem code to report if the header record is not valid,
        defaults to `HEADER_CHECK_FAILED`

        `message` - problem message to report if a value is not valid

        """

        t = code, message
        self._header_checks.append(t)


    def add_record_length_check(self,
                         code=RECORD_LENGTH_CHECK_FAILED,
                         message=MESSAGES[RECORD_LENGTH_CHECK_FAILED],
                         modulus=1):
        """
        Add a record length check, i.e., check whether the length of a record is
        consistent with the number of expected fields.

        Arguments
        ---------

        `code` - problem code to report if a record is not valid, defaults to
        `RECORD_LENGTH_CHECK_FAILED`

        `message` - problem message to report if a record is not valid

        `modulus` - apply the check to every nth record, defaults to 1 (check
        every record)

        """

        t = code, message, modulus
        self._record_length_checks.append(t)


    def add_value_check(self, field_name, value_check,
                        code=VALUE_CHECK_FAILED,
                        message=MESSAGES[VALUE_CHECK_FAILED],
                        modulus=1):
        """
        Add a value check function for the specified field.

        Arguments
        ---------

        `field_name` - the name of the field to attach the value check function
        to

        `value_check` - a function that accepts a single argument (a value) and
        raises a `ValueError` if the value is not valid

        `code` - problem code to report if a value is not valid, defaults to
        `VALUE_CHECK_FAILED`

        `message` - problem message to report if a value is not valid

        `modulus` - apply the check to every nth record, defaults to 1 (check
        every record)

        """

        # guard conditions
        assert field_name in self._field_names, 'unexpected field name: %s' % field_name
        assert callable(value_check), 'value check must be a callable function'

        t = field_name, value_check, code, message, modulus
        self._value_checks.append(t)


    def add_value_predicate(self, field_name, value_predicate,
                        code=VALUE_PREDICATE_FALSE,
                        message=MESSAGES[VALUE_PREDICATE_FALSE],
                        modulus=1):
        """
        Add a value predicate function for the specified field.

        N.B., everything you can do with value predicates can also be done with
        value check functions, whether you use one or the other is a matter of
        style.

        Arguments
        ---------

        `field_name` - the name of the field to attach the value predicate
        function to

        `value_predicate` - a function that accepts a single argument (a value)
        and returns False if the value is not valid

        `code` - problem code to report if a value is not valid, defaults to
        `VALUE_PREDICATE_FALSE`

        `message` - problem message to report if a value is not valid

        `modulus` - apply the check to every nth record, defaults to 1 (check
        every record)

        """

        assert field_name in self._field_names, 'unexpected field name: %s' % field_name
        assert callable(value_predicate), 'value predicate must be a callable function'

        t = field_name, value_predicate, code, message, modulus
        self._value_predicates.append(t)


    def add_record_check(self, record_check, modulus=1):
        """
        Add a record check function.

        Arguments
        ---------

        `record_check` - a function that accepts a single argument (a record as
        a dictionary of values indexed by field name) and raises a
        `RecordError` if the record is not valid

        `modulus` - apply the check to every nth record, defaults to 1 (check
        every record)

        """

        assert callable(record_check), 'record check must be a callable function'

        t = record_check, modulus
        self._record_checks.append(t)


    def add_record_predicate(self, record_predicate,
                        code=RECORD_PREDICATE_FALSE,
                        message=MESSAGES[RECORD_PREDICATE_FALSE],
                        modulus=1):
        """
        Add a record predicate function.

        N.B., everything you can do with record predicates can also be done with
        record check functions, whether you use one or the other is a matter of
        style.

        Arguments
        ---------

        `record_predicate` - a function that accepts a single argument (a record
        as a dictionary of values indexed by field name) and returns False if
        the value is not valid

        `code` - problem code to report if a record is not valid, defaults to
        `RECORD_PREDICATE_FALSE`

        `message` - problem message to report if a record is not valid

        `modulus` - apply the check to every nth record, defaults to 1 (check
        every record)

        """

        assert callable(record_predicate), 'record predicate must be a callable function'

        t = record_predicate, code, message, modulus
        self._record_predicates.append(t)


    def add_unique_check(self, key,
                        code=UNIQUE_CHECK_FAILED,
                        message=MESSAGES[UNIQUE_CHECK_FAILED]):
        """
        Add a unique check on a single column or combination of columns.

        Arguments
        ---------

        `key` - a single field name (string) specifying a field in which all
        values are expected to be unique, or a sequence of field names (tuple
        or list of strings) specifying a compound key

        `code` - problem code to report if a record is not valid, defaults to
        `UNIQUE_CHECK_FAILED`

        `message` - problem message to report if a record is not valid

        """

        if isinstance(key, basestring):
            assert key in self._field_names, 'unexpected field name: %s' % key
        else:
            for f in key:
                assert f in self._field_names, 'unexpected field name: %s' % key
        t = key, code, message
        self._unique_checks.append(t)


    def add_skip(self, skip):
        """
        Add a `skip` function which accepts a single argument (a record as a
        sequence of values) and returns True if all checks on the record should
        be skipped.

        """

        assert callable(skip), 'skip must be a callable function'
        self._skips.append(skip)


    def validate(self, data,
                 expect_header_row=True,
                 ignore_lines=0,
                 summarize=False,
                 limit=0,
                 context=None,
                 report_unexpected_exceptions=True):
        """
        Validate `data` and return a list of validation problems found.

        Arguments
        ---------

        `data` - any source of row-oriented data, e.g., as provided by a
        `csv.reader`, or a list of lists of strings, or ...

        `expect_header_row` - does the data contain a header row (i.e., the
        first record is a list of field names)? Defaults to True.

        `ignore_lines` - ignore n lines (rows) at the beginning of the data

        `summarize` - only report problem codes, no other details

        `limit` - report at most n problems

        `context` - a dictionary of any additional information to be added to
        any problems found - useful if problems are being aggregated from
        multiple validators

        `report_unexpected_exceptions` - value check function, value predicates,
        record check functions, record predicates, and other user-supplied
        validation functions may raise unexpected exceptions. If this argument
        is true, any unexpected exceptions will be reported as validation
        problems; if False, unexpected exceptions will be handled silently.

        """

        problems = list()
        problem_generator = self.ivalidate(data, expect_header_row,
                                           ignore_lines, summarize, context,
                                           report_unexpected_exceptions)
        for i, p in enumerate(problem_generator):
            if not limit or i < limit:
                problems.append(p)
        return problems


    def ivalidate(self, data,
                 expect_header_row=True,
                 ignore_lines=0,
                 summarize=False,
                 context=None,
                 report_unexpected_exceptions=True):
        """
        Validate `data` and return a iterator over problems found.

        Use this function rather than validate() if you expect a large number
        of problems.

        Arguments
        ---------

        `data` - any source of row-oriented data, e.g., as provided by a
        `csv.reader`, or a list of lists of strings, or ...

        `expect_header_row` - does the data contain a header row (i.e., the
        first record is a list of field names)? Defaults to True.

        `ignore_lines` - ignore n lines (rows) at the beginning of the data

        `summarize` - only report problem codes, no other details

        `context` - a dictionary of any additional information to be added to
        any problems found - useful if problems are being aggregated from
        multiple validators

        `report_unexpected_exceptions` - value check function, value predicates,
        record check functions, record predicates, and other user-supplied
        validation functions may raise unexpected exceptions. If this argument
        is true, any unexpected exceptions will be reported as validation
        problems; if False, unexpected exceptions will be handled silently.

        """

        unique_sets = self._init_unique_sets() # used for unique checks
        for i, r in enumerate(data):
            if expect_header_row and i == ignore_lines:
                # r is the header row
                for p in self._apply_header_checks(i, r, summarize, context):
                    yield p
            elif i >= ignore_lines:
                # r is a data row
                skip = False
                for p in self._apply_skips(i, r, summarize,
                                                  report_unexpected_exceptions,
                                                  context):
                    if p is True:
                        skip = True
                    else:
                        yield p
                if not skip:
                    for p in self._apply_each_methods(i, r, summarize,
                                                      report_unexpected_exceptions,
                                                      context):
                        yield p # may yield a problem if an exception is raised
                    for p in self._apply_value_checks(i, r, summarize,
                                                      report_unexpected_exceptions,
                                                      context):
                        yield p
                    for p in self._apply_record_length_checks(i, r, summarize,
                                                              context):
                        yield p
                    for p in self._apply_value_predicates(i, r, summarize,
                                                          report_unexpected_exceptions,
                                                          context):
                        yield p
                    for p in self._apply_record_checks(i, r, summarize,
                                                           report_unexpected_exceptions,
                                                           context):
                        yield p
                    for p in self._apply_record_predicates(i, r, summarize,
                                                           report_unexpected_exceptions,
                                                           context):
                        yield p
                    for p in self._apply_unique_checks(i, r, unique_sets, summarize):
                        yield p
                    for p in self._apply_check_methods(i, r, summarize,
                                                       report_unexpected_exceptions,
                                                       context):
                        yield p
                    for p in self._apply_assert_methods(i, r, summarize,
                                                        report_unexpected_exceptions,
                                                        context):
                        yield p
        for p in self._apply_finally_assert_methods(summarize,
                                                    report_unexpected_exceptions,
                                                    context):
            yield p


    def _init_unique_sets(self):
        """Initialise sets used for uniqueness checking."""

        ks = dict()
        for t in self._unique_checks:
            key = t[0]
            ks[key] = set() # empty set
        return ks


    def _apply_value_checks(self, i, r,
                            summarize=False,
                            report_unexpected_exceptions=True,
                            context=None):
        """Apply value check functions on the given record `r`."""

        for field_name, check, code, message, modulus in self._value_checks:
            if i % modulus == 0: # support sampling
                fi = self._field_names.index(field_name)
                if fi < len(r): # only apply checks if there is a value
                    value = r[fi]
                    try:
                        check(value)
                    except ValueError:
                        p = {'code': code}
                        if not summarize:
                            p['message'] = message
                            p['row'] = i + 1
                            p['column'] = fi + 1
                            p['field'] = field_name
                            p['value'] = value
                            p['record'] = r
                            if context is not None: p['context'] = context
                        yield p
                    except Exception as e:
                        if report_unexpected_exceptions:
                            p = {'code': UNEXPECTED_EXCEPTION}
                            if not summarize:
                                p['message'] = MESSAGES[UNEXPECTED_EXCEPTION] % (e.__class__.__name__, e)
                                p['row'] = i + 1
                                p['column'] = fi + 1
                                p['field'] = field_name
                                p['value'] = value
                                p['record'] = r
                                p['exception'] = e
                                p['function'] = '%s: %s' % (check.__name__,
                                                            check.__doc__)
                                if context is not None: p['context'] = context
                            yield p


    def _apply_header_checks(self, i, r, summarize=False, context=None):
        """Apply header checks on the given record `r`."""

        for code, message in self._header_checks:
            if tuple(r) != self._field_names:
                p = {'code': code}
                if not summarize:
                    p['message'] = message
                    p['row'] = i + 1
                    p['record'] = tuple(r)
                    p['missing'] = set(self._field_names) - set(r)
                    p['unexpected'] = set(r) - set(self._field_names)
                    if context is not None: p['context'] = context
                yield p


    def _apply_record_length_checks(self, i, r, summarize=False, context=None):
        """Apply record length checks on the given record `r`."""

        for code, message, modulus in self._record_length_checks:
            if i % modulus == 0: # support sampling
                if len(r) != len(self._field_names):
                    p = {'code': code}
                    if not summarize:
                        p['message'] = message
                        p['row'] = i + 1
                        p['record'] = r
                        p['length'] = len(r)
                        if context is not None: p['context'] = context
                    yield p


    def _apply_value_predicates(self, i, r,
                                summarize=False,
                                report_unexpected_exceptions=True,
                                context=None):
        """Apply value predicates on the given record `r`."""

        for field_name, predicate, code, message, modulus in self._value_predicates:
            if i % modulus == 0: # support sampling
                fi = self._field_names.index(field_name)
                if fi < len(r): # only apply predicate if there is a value
                    value = r[fi]
                    try:
                        valid = predicate(value)
                        if not valid:
                            p = {'code': code}
                            if not summarize:
                                p['message'] = message
                                p['row'] = i + 1
                                p['column'] = fi + 1
                                p['field'] = field_name
                                p['value'] = value
                                p['record'] = r
                                if context is not None: p['context'] = context
                            yield p
                    except Exception as e:
                        if report_unexpected_exceptions:
                            p = {'code': UNEXPECTED_EXCEPTION}
                            if not summarize:
                                p['message'] = MESSAGES[UNEXPECTED_EXCEPTION] % (e.__class__.__name__, e)
                                p['row'] = i + 1
                                p['column'] = fi + 1
                                p['field'] = field_name
                                p['value'] = value
                                p['record'] = r
                                p['exception'] = e
                                p['function'] = '%s: %s' % (predicate.__name__,
                                                            predicate.__doc__)
                                if context is not None: p['context'] = context
                            yield p


    def _apply_record_checks(self, i, r,
                                 summarize=False,
                                 report_unexpected_exceptions=True,
                                 context=None):
        """Apply record checks on `r`."""

        for check, modulus in self._record_checks:
            if i % modulus == 0: # support sampling
                rdict = self._as_dict(r)
                try:
                    check(rdict)
                except RecordError as e:
                    code = e.code if e.code is not None else RECORD_CHECK_FAILED
                    p = {'code': code}
                    if not summarize:
                        message = e.message if e.message is not None else MESSAGES[RECORD_CHECK_FAILED]
                        p['message'] = message
                        p['row'] = i + 1
                        p['record'] = r
                        if context is not None: p['context'] = context
                        if e.details is not None: p['details'] = e.details
                    yield p
                except Exception as e:
                    if report_unexpected_exceptions:
                        p = {'code': UNEXPECTED_EXCEPTION}
                        if not summarize:
                            p['message'] = MESSAGES[UNEXPECTED_EXCEPTION] % (e.__class__.__name__, e)
                            p['row'] = i + 1
                            p['record'] = r
                            p['exception'] = e
                            p['function'] = '%s: %s' % (check.__name__,
                                                        check.__doc__)
                            if context is not None: p['context'] = context
                        yield p


    def _apply_record_predicates(self, i, r,
                                 summarize=False,
                                 report_unexpected_exceptions=True,
                                 context=None):
        """Apply record predicates on `r`."""

        for predicate, code, message, modulus in self._record_predicates:
            if i % modulus == 0: # support sampling
                rdict = self._as_dict(r)
                try:
                    valid = predicate(rdict)
                    if not valid:
                        p = {'code': code}
                        if not summarize:
                            p['message'] = message
                            p['row'] = i + 1
                            p['record'] = r
                            if context is not None: p['context'] = context
                        yield p
                except Exception as e:
                    if report_unexpected_exceptions:
                        p = {'code': UNEXPECTED_EXCEPTION}
                        if not summarize:
                            p['message'] = MESSAGES[UNEXPECTED_EXCEPTION] % (e.__class__.__name__, e)
                            p['row'] = i + 1
                            p['record'] = r
                            p['exception'] = e
                            p['function'] = '%s: %s' % (predicate.__name__,
                                                        predicate.__doc__)
                            if context is not None: p['context'] = context
                        yield p


    def _apply_unique_checks(self, i, r, unique_sets,
                             summarize=False,
                             context=None):
        """Apply unique checks on `r`."""

        for key, code, message in self._unique_checks:
            value = None
            values = unique_sets[key]
            if isinstance(key, basestring): # assume key is a field name
                fi = self._field_names.index(key)
                if fi >= len(r):
                    continue
                value = r[fi]
            else: # assume key is a list or tuple, i.e., compound key
                value = []
                for f in key:
                    fi = self._field_names.index(f)
                    if fi >= len(r):
                        break
                    value.append(r[fi])
                value = tuple(value) # enable hashing
            if value in values:
                p = {'code': code}
                if not summarize:
                    p['message'] = message
                    p['row'] = i + 1
                    p['record'] = r
                    p['key'] = key
                    p['value'] = value
                    if context is not None: p['context'] = context
                yield p
            values.add(value)


    def _apply_each_methods(self, i, r,
                            summarize=False,
                            report_unexpected_exceptions=True,
                            context=None):
        """Invoke 'each' methods on `r`."""

        for a in dir(self):
            if a.startswith('each'):
                rdict = self._as_dict(r)
                f = getattr(self, a)
                try:
                    f(rdict)
                except Exception as e:
                    if report_unexpected_exceptions:
                        p = {'code': UNEXPECTED_EXCEPTION}
                        if not summarize:
                            p['message'] = MESSAGES[UNEXPECTED_EXCEPTION] % (e.__class__.__name__, e)
                            p['row'] = i + 1
                            p['record'] = r
                            p['exception'] = e
                            p['function'] = '%s: %s' % (f.__name__,
                                                        f.__doc__)
                            if context is not None: p['context'] = context
                        yield p


    def _apply_assert_methods(self, i, r,
                              summarize=False,
                              report_unexpected_exceptions=True,
                              context=None):
        """Apply 'assert' methods on `r`."""

        for a in dir(self):
            if a.startswith('assert'):
                rdict = self._as_dict(r)
                f = getattr(self, a)
                try:
                    f(rdict)
                except AssertionError as e:
                    code = ASSERT_CHECK_FAILED
                    message = MESSAGES[ASSERT_CHECK_FAILED]
                    if len(e.args) > 0:
                        custom = e.args[0]
                        if isinstance(custom, (list, tuple)):
                            if len(custom) > 0:
                                code = custom[0]
                            if len(custom) > 1:
                                message = custom[1]
                        else:
                            code = custom
                    p = {'code': code}
                    if not summarize:
                        p['message'] = message
                        p['row'] = i + 1
                        p['record'] = r
                        if context is not None: p['context'] = context
                    yield p
                except Exception as e:
                    if report_unexpected_exceptions:
                        p = {'code': UNEXPECTED_EXCEPTION}
                        if not summarize:
                            p['message'] = MESSAGES[UNEXPECTED_EXCEPTION] % (e.__class__.__name__, e)
                            p['row'] = i + 1
                            p['record'] = r
                            p['exception'] = e
                            p['function'] = '%s: %s' % (f.__name__,
                                                        f.__doc__)
                            if context is not None: p['context'] = context
                        yield p


    def _apply_check_methods(self, i, r,
                              summarize=False,
                              report_unexpected_exceptions=True,
                              context=None):
        """Apply 'check' methods on `r`."""

        for a in dir(self):
            if a.startswith('check'):
                rdict = self._as_dict(r)
                f = getattr(self, a)
                try:
                    f(rdict)
                except RecordError as e:
                    code = e.code if e.code is not None else RECORD_CHECK_FAILED
                    p = {'code': code}
                    if not summarize:
                        message = e.message if e.message is not None else MESSAGES[RECORD_CHECK_FAILED]
                        p['message'] = message
                        p['row'] = i + 1
                        p['record'] = r
                        if context is not None: p['context'] = context
                        if e.details is not None: p['details'] = e.details
                    yield p
                except Exception as e:
                    if report_unexpected_exceptions:
                        p = {'code': UNEXPECTED_EXCEPTION}
                        if not summarize:
                            p['message'] = MESSAGES[UNEXPECTED_EXCEPTION] % (e.__class__.__name__, e)
                            p['row'] = i + 1
                            p['record'] = r
                            p['exception'] = e
                            p['function'] = '%s: %s' % (f.__name__,
                                                        f.__doc__)
                            if context is not None: p['context'] = context
                        yield p


    def _apply_finally_assert_methods(self,
                                      summarize=False,
                                      report_unexpected_exceptions=True,
                                      context=None):
        """Apply 'finally_assert' methods."""

        for a in dir(self):
            if a.startswith('finally_assert'):
                f = getattr(self, a)
                try:
                    f()
                except AssertionError as e:
                    code = ASSERT_CHECK_FAILED
                    message = MESSAGES[ASSERT_CHECK_FAILED]
                    if len(e.args) > 0:
                        custom = e.args[0]
                        if isinstance(custom, (list, tuple)):
                            if len(custom) > 0:
                                code = custom[0]
                            if len(custom) > 1:
                                message = custom[1]
                        else:
                            code = custom
                    p = {'code': code}
                    if not summarize:
                        p['message'] = message
                        if context is not None: p['context'] = context
                    yield p
                except Exception as e:
                    if report_unexpected_exceptions:
                        p = {'code': UNEXPECTED_EXCEPTION}
                        if not summarize:
                            p['message'] = MESSAGES[UNEXPECTED_EXCEPTION] % (e.__class__.__name__, e)
                            p['exception'] = e
                            p['function'] = '%s: %s' % (f.__name__,
                                                        f.__doc__)
                            if context is not None: p['context'] = context
                        yield p


    def _apply_skips(self, i, r,
                     summarize=False,
                     report_unexpected_exceptions=True,
                     context=None):
        """Apply skip functions on `r`."""

        for skip in self._skips:
            try:
                result = skip(r)
                if result is True:
                    yield True
            except Exception as e:
                if report_unexpected_exceptions:
                    p = {'code': UNEXPECTED_EXCEPTION}
                    if not summarize:
                        p['message'] = MESSAGES[UNEXPECTED_EXCEPTION] % (e.__class__.__name__, e)
                        p['row'] = i + 1
                        p['record'] = r
                        p['exception'] = e
                        p['function'] = '%s: %s' % (skip.__name__,
                                                    skip.__doc__)
                        if context is not None: p['context'] = context
                    yield p


    def _as_dict(self, r):
        """Convert the record to a dictionary using field names as keys."""

        d = dict()
        for i, f in enumerate(self._field_names):
            d[f] = r[i] if i < len(r) else None
        return d


def enumeration(*args):
    """
    Return a value check function which raises a value error if the value is not
    in a pre-defined enumeration of values.

    If you pass in a list, tuple or set as the single argument, it is assumed
    that the list/tuple/set defines the membership of the enumeration.

    If you pass in more than on argument, it is assumed the arguments themselves
    define the enumeration.

    """

    assert len(args) > 0, 'at least one argument is required'
    if len(args) == 1:
        # assume the first argument defines the membership
        members = args[0]
    else:
        # assume the arguments are the members
        members = args
    def checker(value):
        if value not in members:
            raise ValueError(value)
    return checker


def match_pattern(regex):
    """
    Return a value check function which raises a ValueError if the value does
    not match the supplied regular expression, see also `re.match`.

    """

    prog = re.compile(regex)
    def checker(v):
        result = prog.match(v)
        if result is None:
            raise ValueError(v)
    return checker


def search_pattern(regex):
    """
    Return a value check function which raises a ValueError if the supplied
    regular expression does not match anywhere in the value, see also
    `re.search`.

    """

    prog = re.compile(regex)
    def checker(v):
        result = prog.search(v)
        if result is None:
            raise ValueError(v)
    return checker


def number_range_inclusive(min, max, type=float):
    """
    Return a value check function which raises a ValueError if the supplied
    value when cast as `type` is less than `min` or greater than `max`.

    """

    def checker(v):
        if type(v) < min or type(v) > max:
            raise ValueError(v)
    return checker


def number_range_exclusive(min, max, type=float):
    """
    Return a value check function which raises a ValueError if the supplied
    value when cast as `type` is less than or equal to `min` or greater than
    or equal to `max`.

    """

    def checker(v):
        if type(v) <= min or type(v) >= max:
            raise ValueError(v)
    return checker


def datetime_string(format):
    """
    Return a value check function which raises a ValueError if the supplied
    value cannot be converted to a datetime using the supplied format string.

    See also `datetime.strptime`.

    """

    def checker(v):
        datetime.strptime(v, format)
    return checker


def datetime_range_inclusive(min, max, format):
    """
    Return a value check function which raises a ValueError if the supplied
    value when converted to a datetime using the supplied `format` string is
    less than `min` or greater than `max`.

    """

    dmin = datetime.strptime(min, format)
    dmax = datetime.strptime(max, format)
    def checker(v):
        dv = datetime.strptime(v, format)
        if dv < dmin or dv > dmax:
            raise ValueError(v)
    return checker


def datetime_range_exclusive(min, max, format):
    """
    Return a value check function which raises a ValueError if the supplied
    value when converted to a datetime using the supplied `format` string is
    less than or equal to `min` or greater than or equal to `max`.

    """

    dmin = datetime.strptime(min, format)
    dmax = datetime.strptime(max, format)
    def checker(v):
        dv = datetime.strptime(v, format)
        if dv <= dmin or dv >= dmax:
            raise ValueError(v)
    return checker


def write_problems(problems, file, summarize=False, limit=0):
    """
    Write problems as restructured text to a file (or stdout/stderr).

    """
    w = file.write # convenience variable
    w("""
=================
Validation Report
=================
""")
    counts = dict() # store problem counts per problem code
    total = 0
    for i, p in enumerate(problems):
        if limit and i >= limit:
            break # bail out
        if total == 0 and not summarize:
            w("""
Problems
========
""")
        total += 1
        code = p['code']
        if code in counts:
            counts[code] += 1
        else:
            counts[code] = 1
        if not summarize:
            ptitle = '\n%s - %s\n' % (p['code'], p['message'])
            w(ptitle)
            underline = ''
            for i in range(len(ptitle.strip())):
                underline += '-'
            underline += '\n'
            w(underline)
            for k in sorted(p.keys() - set(['code', 'message', 'context'])):
                w(':%s: %s\n' % (k, p[k]))
            if 'context' in p:
                c = p['context']
                for k in sorted(c.keys()):
                    w(':%s: %s\n' % (k, c[k]))

    w("""
Summary
=======

Found %s%s problem%s in total.

""" % ('at least ' if limit else '', total, 's' if total != 1 else ''))
    for code in sorted(counts.keys()):
        w(':%s: %s\n' % (code, counts[code]))
    return total


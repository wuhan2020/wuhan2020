import { createCell, Fragment } from 'web-cell';
import { parseTextTable } from 'boot-cell/source/utility';
import { Table } from 'boot-cell/source/Content/Table';

import data from '../../data/HOSPITAL.csv';

interface Contact {
    name: string;
    numbers: string[];
}

interface Hospital {
    name: string;
    url: string;
    address: string;
    size: number;
    supplies: string | string[];
    contact?: string | Contact[];
    remark: string;
}

const list = parseTextTable(data, true).map(
    ({ contact, supplies = '', ...rest }: Hospital) => ({
        ...rest,
        supplies: (supplies as string).split(';'),
        contact: (contact as string)?.split(';').map(item => {
            const [name, ...numbers] = item.split('|');

            return { name, numbers };
        })
    })
);

function HospitalItem({
    name,
    url,
    address,
    size,
    supplies = [],
    contact,
    remark
}: Hospital) {
    return (
        <tr>
            <td className="text-nowrap">
                {url ? (
                    <a target="_blank" href={url}>
                        {name}
                    </a>
                ) : (
                    name
                )}
            </td>
            <td>{address}</td>
            <td>{size}</td>
            <td className="text-left">
                <ol>
                    {(supplies as string[]).map(item => (
                        <li>{item}</li>
                    ))}
                </ol>
            </td>
            <td className="text-nowrap">
                {contact && (
                    <ul className="list-unstyled">
                        {(contact as Contact[]).map(({ name, numbers }) => (
                            <li>
                                {name}：
                                {numbers.map((item, index) => (
                                    <a
                                        className="mx-1"
                                        href={'tel:+86-' + item}
                                    >
                                        电话
                                        {++index}
                                    </a>
                                ))}
                            </li>
                        ))}
                    </ul>
                )}
            </td>
            <td>{remark}</td>
        </tr>
    );
}

export function HospitalPage() {
    return (
        <Fragment>
            <h2>医院急需物资</h2>

            <Table center striped hover>
                <thead>
                    <tr>
                        <th>名称</th>
                        <th>地址</th>
                        <th>规模</th>
                        <th>急需物资</th>
                        <th>联系方式</th>
                        <th>备注</th>
                    </tr>
                </thead>
                <tbody>{list.map(HospitalItem)}</tbody>
            </Table>
        </Fragment>
    );
}

import * as clipboard from 'clipboard-polyfill';
import { createCell, Fragment } from 'web-cell';
import { Table } from 'boot-cell/source/Content/Table';
import { Button } from 'boot-cell/source/Form/Button';

import list from '../../data/Hospital.yml';

interface Contact {
    name: string;
    numbers: string[];
}

interface Hospital {
    name: string;
    url: string;
    address: string;
    size: number;
    supplies: string[];
    contact?: Contact[];
    remark: string;
}

function HospitalItem({
    name,
    url,
    address,
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
            <td>
                <Button onClick={() => clipboard.writeText(address)}>
                    复制
                </Button>
            </td>
            <td className="text-left">
                <ol>
                    {supplies.map(item => (
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

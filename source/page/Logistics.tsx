import { createCell, Fragment } from 'web-cell';
import { Table } from 'boot-cell/source/Content/Table';
import { Button } from 'boot-cell/source/Form/Button';

import list from '../../data/Logistics.yml';

interface Logistics {
    name: string;
    url: string;
    area: string;
    capability: string;
    phones: string[];
}

export function LogisticsPage() {
    return (
        <Fragment>
            <h2>物流公司</h2>

            <Table center striped hover>
                <thead>
                    <tr>
                        <th>名称</th>
                        <th>区域</th>
                        <th>能力</th>
                        <th>电话</th>
                    </tr>
                </thead>
                <tbody>
                    {list.map(
                        ({
                            url,
                            name,
                            area,
                            capability,
                            phones
                        }: Logistics) => (
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
                                <td className="text-nowrap">{area}</td>
                                <td className="text-nowrap">{capability}</td>
                                <td>
                                    <div className="btn-group">
                                        {phones.map(item => (
                                            <Button href={'tel:' + item}>
                                                {item}
                                            </Button>
                                        ))}
                                    </div>
                                </td>
                            </tr>
                        )
                    )}
                </tbody>
            </Table>
        </Fragment>
    );
}

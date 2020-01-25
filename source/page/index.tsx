import { component, createCell, Fragment } from 'web-cell';
import { observer } from 'mobx-web-cell';
import { HTMLRouter } from 'cell-router/source';
import { NavBar } from 'boot-cell/source/Navigator/NavBar';

import { history } from '../model';
import { HomePage } from './Home';
import { HospitalPage } from './Hospital';
import { LogisticsPage } from './Logistics';

@observer
@component({
    tagName: 'page-router',
    renderTarget: 'children'
})
export class PageRouter extends HTMLRouter {
    protected history = history;
    protected routes = [
        { paths: [''], component: HomePage },
        { paths: ['hospital'], component: HospitalPage },
        { paths: ['logistics'], component: LogisticsPage }
    ];

    menu = [
        {
            title: '首页',
            href: ''
        },
        {
            title: '医院',
            href: 'hospital'
        },
        {
            title: '物流',
            href: 'logistics'
        },
        {
            title: '开放源代码',
            href: 'https://github.com/EasyWebApp/wuhan2020'
        }
    ];

    render() {
        return (
            <Fragment>
                <NavBar title="2020 援助武汉" menu={this.menu} narrow />

                <main
                    className="container my-5 pt-3"
                    style={{ minHeight: '60vh' }}
                >
                    {super.render()}
                </main>

                <footer className="text-center bg-light py-5">
                    Proudly developed with
                    <a
                        className="mx-1"
                        target="_blank"
                        href="https://web-cell.dev/"
                    >
                        WebCell v2
                    </a>
                    &amp;
                    <a
                        className="mx-1"
                        target="_blank"
                        href="https://web-cell.dev/BootCell/"
                    >
                        BootCell v1
                    </a>
                </footer>
            </Fragment>
        );
    }
}

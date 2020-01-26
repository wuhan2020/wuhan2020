import { createCell } from 'web-cell';
import { Jumbotron } from 'boot-cell/source/Content/Jumbotron';

export function HomePage() {
    return (
        <Jumbotron
            title="2020 援助武汉"
            description="新冠病毒疫情中的武汉援助信息网站"
        />
    );
}

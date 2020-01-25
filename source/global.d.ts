declare module '*.csv' {
    const content: string;

    export default content;
}

declare module '*.yml' {
    const data: { [key: string]: any };

    export default data;
}

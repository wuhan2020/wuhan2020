import { auto } from 'browser-unhandled-rejection';
import { documentReady, render, createCell } from 'web-cell';

import { PageRouter } from './page';

if ('serviceWorker' in navigator) navigator.serviceWorker.register('./sw.ts');

auto();

self.addEventListener('unhandledrejection', event => {
    const { message } = event.reason;

    if (!message) return;

    event.preventDefault();

    self.alert(message);
});

documentReady.then(() => render(<PageRouter />));

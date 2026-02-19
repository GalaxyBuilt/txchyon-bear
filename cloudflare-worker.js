// Cloudflare Worker Routing Logic
// This script should be updated in your Cloudflare Worker to route requests between the main blog and the bear blog.

export default {
    async fetch(request, env, ctx) {
        const url = new URL(request.url);
        const pathname = url.pathname;

        // Routing Logic for Txchyon Bear
        if (pathname.startsWith('/bear')) {
            // Route to txchyon-bear deployment
            // Replace with your actual bear blog origin (e.g., a Cloudflare Pages preview URL or a specific worker origin)
            const bearOrigin = "https://bear.txchyon.pages.dev";
            const bearUrl = new URL(pathname + url.search, bearOrigin);

            return fetch(new Request(bearUrl, request));
        }

        // Default: Route to main Txchyon deployment
        const mainOrigin = "https://main.txchyon.pages.dev";
        const mainUrl = new URL(pathname + url.search, mainOrigin);

        return fetch(new Request(mainUrl, request));
    }
};

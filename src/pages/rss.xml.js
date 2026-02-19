import rss from "@astrojs/rss";
import { getCollection } from "astro:content";

export const GET = async ({ site }) => {
    if (!site) {
        return new Response("Site URL not configured", { status: 500 });
    }

    const posts = await getCollection("posts", ({ data }) => !data.draft);

    return rss({
        title: "Defensive Intelligence Division",
        description: "Defensive market intelligence, systemic risk analysis, and capital preservation frameworks.",
        site: site + (site.toString().endsWith('/') ? 'bear' : '/bear'),
        stylesheet: false,
        customData: `<language>en-us</language>`,
        items: posts.map((post) => {
            // Ensure the link is relative to the /bear base
            const link = `/bear/blog/${post.slug}/`;

            return {
                title: post.data.title || "Untitled Assessment",
                description: post.data.description || "Defensive analyst report from Txchyon Bear Division",
                link: link,
                pubDate: new Date(post.data.date),
            };
        }),
    });
};

import { getCollection } from 'astro:content';

export const GET = async ({ site }) => {
    if (!site) {
        return new Response('Site URL not configured', { status: 500 });
    }

    const posts = await getCollection('posts', ({ data }) => !data.draft);

    const items = posts
        .map((post) => {
            const url = new URL(`/bear/blog/${post.slug}/`, site).href;
            const imageUrl = post.data.image
                ? new URL(
                    post.data.image.startsWith('/') ? post.data.image : `/bear${post.data.image.startsWith('/') ? '' : '/'}${post.data.image}`,
                    site
                ).href
                : undefined;

            return {
                id: url,
                url,
                title: post.data.title || 'Untitled Assessment',
                summary: post.data.description || 'Defensive analyst report from Txchyon Bear Division',
                date_published: new Date(post.data.date).toISOString(),
                image: imageUrl,
            };
        })
        .sort((a, b) => new Date(b.date_published).getTime() - new Date(a.date_published).getTime());

    return new Response(
        JSON.stringify(
            {
                version: 'https://jsonfeed.org/version/1.1',
                title: "Defensive Intelligence Division",
                description: 'Defensive market intelligence, systemic risk analysis, and capital preservation frameworks.',
                home_page_url: new URL('/bear/', site).href,
                feed_url: new URL('/bear/feed.json', site).href,
                items,
            },
            null,
            2
        ),
        {
            headers: {
                'Content-Type': 'application/feed+json; charset=utf-8',
            },
        }
    );
};

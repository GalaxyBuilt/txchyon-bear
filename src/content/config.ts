import { defineCollection, z } from 'astro:content';

const bearBlogCategories = [
    'macro-liquidity',
    'systemic-risk',
    'fraud-red-flags',
    'bearish-frameworks',
    'crowd-psychology',
    'capital-preservation'
] as const;

const postsCollection = defineCollection({
    type: 'content',
    schema: z.object({
        title: z.string(),
        description: z.string(),
        date: z.coerce.date(),
        pillar: z.enum(bearBlogCategories),
        subcategory: z.string(),
        tags: z.array(z.string()).default([]),
        draft: z.boolean().default(false),
        hasGatedContent: z.boolean().default(false),
        isFullyGated: z.boolean().default(false),
        image: z.string().optional(),
        author: z.string().default('galaxybuilt'),
    }).passthrough(),
});

export const collections = {
    posts: postsCollection,
};

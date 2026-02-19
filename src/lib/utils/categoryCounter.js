// src/lib/utils/categoryCounter.js
import { getCollection } from "astro:content";

export async function getCategoriesWithCounts() {
  try {
    const posts = await getCollection("posts");
    const categoryCounts = {};
    
    // Count posts by CATEGORY (not tags)
    posts.forEach(post => {
      if (post.data.categories) {
        post.data.categories.forEach(category => {
          const catName = String(category).trim();
          categoryCounts[catName] = (categoryCounts[catName] || 0) + 1;
        });
      }
    });
    
    // Convert to array and sort by count (descending)
    const sortedCategories = Object.entries(categoryCounts)
      .map(([name, count]) => ({ name, count }))
      .sort((a, b) => b.count - a.count);
    
    return sortedCategories;
  } catch (error) {
    console.error("Error counting categories:", error);
    return [];
  }
}

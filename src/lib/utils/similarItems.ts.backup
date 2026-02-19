// Find similar posts based on SINGULAR category and tags
const similarItems = (currentItem: any, allItems: any, currentSlug: string) => {
  // Get current post's SINGULAR category and tags
  const currentCategory = currentItem.data.category; // SINGULAR
  const currentTags = currentItem.data.tags || [];
  
  // Safety checks
  if (!currentCategory && currentTags.length === 0) {
    return []; // No data to compare
  }

  // Filter out current post and drafts
  const otherItems = allItems.filter(
    (item: any) => 
      item.slug !== currentSlug && 
      !item.data.draft
  );

  let similar = [];
  
  // 1. First try: Same category (most important)
  if (currentCategory) {
    const sameCategory = otherItems.filter(
      (item: any) => item.data.category === currentCategory
    );
    similar = [...similar, ...sameCategory];
  }
  
  // 2. Second try: Same tags (if we need more)
  if (similar.length < 3 && currentTags.length > 0) {
    const sameTags = otherItems
      .filter((item: any) => {
        if (similar.some(s => s.slug === item.slug)) return false; // Skip already added
        const itemTags = item.data.tags || [];
        return itemTags.some((tag: string) => currentTags.includes(tag));
      })
      .slice(0, 3 - similar.length); // Only take as many as needed
    
    similar = [...similar, ...sameTags];
  }
  
  // 3. Last resort: Random posts from same category or any
  if (similar.length < 3) {
    const remaining = otherItems
      .filter((item: any) => !similar.some(s => s.slug === item.slug))
      .slice(0, 3 - similar.length);
    
    similar = [...similar, ...remaining];
  }
  
  return similar.slice(0, 3); // Max 3 similar posts
};

export default similarItems;
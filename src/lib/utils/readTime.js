// src/utils/readTime.js

export function calculateReadTime(content, wordsPerMinute = 130) {
  // Remove code blocks, frontmatter, and HTML tags for accurate word count
  const plainText = content
    .replace(/---[\s\S]*?---/, '') // Remove frontmatter
    .replace(/```[\s\S]*?```/g, '') // Remove code blocks
    .replace(/<[^>]*>/g, '') // Remove HTML tags
    .replace(/#{1,6}\s*/g, '') // Remove markdown headers
    .replace(/[\[\]\(\)]/g, ' ') // Replace brackets with spaces
    .replace(/\s+/g, ' ') // Normalize whitespace
    .trim();
  
  const wordCount = plainText.split(/\s+/).length;
  const minutes = Math.ceil(wordCount / wordsPerMinute);
  
  // Cap at reasonable min/max
  return Math.max(1, Math.min(minutes, 60));
}

// For MDX/Markdown content
export function getPostReadTime(post) {
  if (post.data.readTime) {
    return post.data.readTime; // Use manual if provided
  }
  
  // Calculate from body content
  if (post.body) {
    return calculateReadTime(post.body);
  }
  
  // Fallback based on pillar/category
  return getEstimatedReadTime(post.data);
}

function getEstimatedReadTime(data) {
  // Smart estimates based on content type
  const estimates = {
    'getting-started': 8,
    'security-privacy': 10,
    'airdrop-farming': 12,
    'defi-yield': 15
  };
  
  return estimates[data.pillar] || 10;
}
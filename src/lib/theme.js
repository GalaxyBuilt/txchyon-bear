// Theme persistence utilities
export const THEME_KEY = 'txchyon-theme';

export function getSavedTheme() {
  if (typeof window === 'undefined') return 'dark'; // Default on server
  
  // Check localStorage
  const saved = localStorage.getItem(THEME_KEY);
  if (saved === 'dark' || saved === 'light') return saved;
  
  // Check system preference
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  return prefersDark ? 'dark' : 'light';
}

export function saveTheme(theme) {
  if (typeof window === 'undefined') return;
  localStorage.setItem(THEME_KEY, theme);
  
  // Update HTML class
  document.documentElement.classList.toggle('dark', theme === 'dark');
}

export function toggleTheme() {
  const current = getSavedTheme();
  const newTheme = current === 'dark' ? 'light' : 'dark';
  saveTheme(newTheme);
  return newTheme;
}

// Initialize theme on load
export function initializeTheme() {
  if (typeof window === 'undefined') return;
  
  const theme = getSavedTheme();
  document.documentElement.classList.toggle('dark', theme === 'dark');
  
  // Dispatch event for theme-aware components
  window.dispatchEvent(new CustomEvent('themechange', { detail: theme }));
}
// src/lib/categories.js - TXCHYON BEAR PILLAR HIERARCHY
export const CATEGORY_HIERARCHY = {
  "bearish-frameworks": {
    name: "Bearish Frameworks",
    description: "Structural models for identifying market peaks, exhaustion, and regime shifts.",
    icon: "📉",
    subcategories: {
      "cyclical-analysis": "Cyclical Analysis",
      "valuation-bubbles": "Valuation Bubbles",
      "leverage-unwind": "Leverage Unwind Models"
    }
  },
  "capital-preservation": {
    name: "Capital Preservation",
    description: "Strategies for protecting principal during high-volatility and contraction phases.",
    icon: "🛡️",
    subcategories: {
      "hedging-strategies": "Hedging Strategies",
      "stablecoin-yield": "Stablecoin Yield",
      "risk-parity": "Risk Parity"
    }
  },
  "crowd-psychology": {
    name: "Crowd Psychology",
    description: "Analyzing sentiment extremes, euphoria, and the transition to panic.",
    icon: "🧠",
    subcategories: {
      "euphoria-tracking": "Euphoria Tracking",
      "panic-dynamics": "Panic Dynamics",
      "social-signals": "Social Signals"
    }
  },
  "fraud-red-flags": {
    name: "Fraud & Red Flags",
    description: "Identifying systemic insolvency, rugpulls, and unsustainable ponzi-nomics.",
    icon: "🚩",
    subcategories: {
      "ponzinomics": "Ponzinomics Analysis",
      "insolvency-detection": "Insolvency Detection",
      "on-chain-forensics": "On-Chain Forensics"
    }
  },
  "macro-liquidity": {
    name: "Macro Liquidity",
    description: "Tracking global dollar flows, monetary policy, and credit contraction.",
    icon: "💧",
    subcategories: {
      "monetary-policy": "Monetary Policy",
      "stablecoin-liquidity": "Stablecoin Liquidity",
      "credit-spreads": "Credit Spreads"
    }
  },
  "systemic-risk": {
    name: "Systemic Risk",
    description: "Monitoring contagion vectors and architectural weaknesses in the financial stack.",
    icon: "⚠️",
    subcategories: {
      "contagion-vectors": "Contagion Vectors",
      "protocol-weakness": "Protocol Weakness",
      "centralization-risk": "Centralization Risk"
    }
  }
};

// Helper: Get display name
export function getCategoryDisplay(categoryPath) {
  if (!categoryPath) return '';

  const [pillar, sub] = categoryPath.split('/');
  const pillarData = CATEGORY_HIERARCHY[pillar];

  if (!pillarData) return categoryPath;

  if (sub && pillarData.subcategories[sub]) {
    return pillarData.name + " > " + pillarData.subcategories[sub];
  }

  return pillarData.name;
}

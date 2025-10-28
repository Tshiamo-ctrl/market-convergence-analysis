import pandas as pd
import json

# Market data
markets = {
    'AI': {'2024': 233.46, '2025': 294.16, '2030': 1060, 'cagr': 29.2},
    'EdTech': {'2024': 163.49, '2025': 184.7, '2030': 348.41, 'cagr': 13.3},
    'HRTech': {'2024': 40.45, '2025': 43.66, '2032': 81.84, 'cagr': 9.2}
}

# Save summary
with open('market_analysis_summary.json', 'w') as f:
    json.dump(markets, f, indent=2)

print("Market analysis complete!")
print(f"Total 2025 market: ${sum([m['2025'] for m in markets.values()]):.2f}B")

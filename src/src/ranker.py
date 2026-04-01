def rank(recipes, min_protein, top_n):
    filtered = [r for r in recipes if r.protein_g >= min_protein]
    return sorted(filtered, key=lambda r: r.protein_g, reverse=True)[:top_n]

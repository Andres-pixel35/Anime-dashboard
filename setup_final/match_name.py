import re
import pandas as pd
from rapidfuzz import fuzz
from config import path_user_csv, path_historical_csv, path_final_csv, type_mappings, sort_final
from setup_final import helpers

def normalize_string(s):
    """Remove special chars, extra spaces, lowercase"""
    s = str(s).lower().strip()
    s = re.sub(r'[^\w\s]', '', s)  # Remove punctuation
    s = re.sub(r'\s+', ' ', s)      # Collapse multiple spaces
    return s

def match_dfs(df1, df2, similarity_threshold=85):
    # Pre-normalize df2 once 
    df2 = df2.copy()
    df2['name_norm'] = df2.iloc[:, 0].apply(normalize_string)
    df2['name_en_norm'] = df2.iloc[:, 1].apply(normalize_string)
    df2['type_norm'] = df2.iloc[:, 2].astype(str).str.strip().str.lower()
    
    # Build hash map for exact matches: {(normalized_name, type): row_index}
    exact_match_dict = {}
    for idx, row in df2.iterrows():
        type_val = row['type_norm']
        # Store by both names
        exact_match_dict[(row['name_norm'], type_val)] = idx
        exact_match_dict[(row['name_en_norm'], type_val)] = idx
    
    matched_rows = []
    unmatched_rows = []
    
    # Phase 1: Exact matching
    for idx, row in df1.iterrows():
        media_type = str(row.iloc[1]).strip().lower()
        
        # Skip if type not in mappings
        if media_type not in type_mappings:
            continue
            
        identifier_norm = normalize_string(row.iloc[0])
        allowed_types = type_mappings[media_type]
        
        # Try exact match for each allowed type
        found = False
        for allowed_type in allowed_types:
            key = (identifier_norm, allowed_type)
            if key in exact_match_dict:
                matched_rows.append(df2.loc[exact_match_dict[key]])
                found = True
                break
        
        if not found:
            unmatched_rows.append((idx, row, identifier_norm, allowed_types))
    
    # Phase 2: Fuzzy matching for unmatched rows only
    for idx, row, identifier_norm, allowed_types in unmatched_rows:
        # Filter df2 by allowed types
        type_matches = df2[df2['type_norm'].isin(allowed_types)]
        
        best_match = None
        best_score = 0
        
        for _, candidate in type_matches.iterrows():
            # Compare with normalized strings
            score1 = fuzz.ratio(identifier_norm, candidate['name_norm'])
            score2 = fuzz.ratio(identifier_norm, candidate['name_en_norm'])
            max_score = max(score1, score2)
            
            if max_score > best_score and max_score >= similarity_threshold:
                best_score = max_score
                best_match = candidate
        
        if best_match is not None:
            matched_rows.append(best_match)
    
    # Create result dataframe (only df2 columns)
    df_result = pd.DataFrame(matched_rows).reset_index(drop=True)
    
    # Drop temporary normalization columns
    if not df_result.empty:
        df_result = df_result.drop(columns=['name_norm', 'name_en_norm', 'type_norm'])
    
    return df_result

def main():
    df1 = pd.read_csv(path_user_csv)
    df2 = pd.read_csv(path_historical_csv)

    df = match_dfs(df1, df2)

    df["complete_duration"] = df["duration"] * df["episodes"]

    df = helpers.sort_final(df, sort_final)

    df.to_csv(path_final_csv, index=False)

if __name__ == "__main__":
    main()



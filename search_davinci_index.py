import whoosh.index
from whoosh.qparser import QueryParser, OrGroup, WildcardPlugin
from blank import ____

# Load the index named 'davinci' in 'davinci_idx' directory
whoosh_idx = whoosh.index.open_dir('davinci_idx', indexname='davinci')

# Define query parser to search the chapter_text field
query_parser = QueryParser('chapter_text',
                           schema=whoosh_idx.schema,
                           group=OrGroup)

# Remove WildcardPlugin from the query parser
query_parser.remove_plugin_class(WildcardPlugin)

# Input a query and parse it
query_text = 'Who painted the Mona Lisa?'
parsed_query = query_parser.parse(query_text)

# Search index and grab top hit
with whoosh_idx.searcher() as searcher:
    search_results = searcher.search(parsed_query, limit=1)
    top_hit = [hit['chapter_text'] for hit in search_results][0]

# Check if known answer is in top hit text
print(f'`"Da Vinci" in top_hit`: {"Da Vinci" in top_hit}')

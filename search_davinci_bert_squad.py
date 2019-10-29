import whoosh.index
from whoosh.qparser import QueryParser, OrGroup, WildcardPlugin
from bert_squad import BertSquad
from blank import ____

# Initial BurtSquad instance
bert_squad = BertSquad()

# Load the index named 'davinci' in 'davinci_idx' directory
whoosh_idx = whoosh.index.open_dir('davinci_idx', indexname='davinci')

# Define query parser to search the chapter_text field
query_parser = QueryParser('chapter_text',
                           schema=whoosh_idx.schema,
                           group=OrGroup)

# Remove WildcardPlugin from the query parser
query_parser.remove_plugin_class(WildcardPlugin)

# Ask the question
question = 'What market does FitBit compete in?'
parsed_query = query_parser.parse(question)

# Search index and grab top hit
with whoosh_idx.searcher() as searcher:
    search_results = searcher.search(parsed_query, limit=3)
    result_texts = [sr['article'] for sr in search_results]
    answers = [bert_squad.ask_question([t], [question]) for t in result_texts]

# Check if known answer is in top hit text
print(f'answers: {answers}')
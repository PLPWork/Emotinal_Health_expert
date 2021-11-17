import ktrain
from ktrain import text

# load 20newsgroups datset into an array
from sklearn.datasets import fetch_20newsgroups
remove = ('headers', 'footers', 'quotes')
newsgroups_train = fetch_20newsgroups(subset='train', remove=remove)
newsgroups_test = fetch_20newsgroups(subset='test', remove=remove)
docs = newsgroups_train.data +  newsgroups_test.data

INDEXDIR = '/tmp/myindex'

text.SimpleQA.initialize_index(INDEXDIR)
text.SimpleQA.index_from_list(docs, INDEXDIR, commit_every=len(docs))

qa = text.SimpleQA(INDEXDIR)


answers = qa.ask('When did the Cassini probe launch?')
qa.display_answers(answers[:5])


answers = qa.ask('What causes computer images to be too dark?')
qa.display_answers(answers[:5])

answers = qa.ask('Who was Jesus Christ?')
qa.display_answers(answers[:5])

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer

#Taking a document to be summarized
doc="""OpenGenus Foundation is an open-source non-profit organization with the aim to enable people to work offline for a longer stretch, reduce the time spent on searching by exploiting the fact that almost 90% of the searches are same for every generation and to make programming more accessible.
OpenGenus is all about positivity and innovation.
Over 1000 people have contributed to our missions and joined our family. We have been sponsored by three great companies namely Discourse, GitHub and DigitalOcean. We run one of the most popular Internship program and open-source projects and have made a positive impact over people's life. """
print(doc)

# For Strings
parser=PlaintextParser.from_string(doc,Tokenizer("english"))
# Using KL
summarizer = LuhnSummarizer()
#Summarize the document with 4 sentences
summary = summarizer(parser.document,2)

for sentence in summary:
    print(sentence)
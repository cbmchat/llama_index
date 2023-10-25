"""Default choice select prompt."""

from llama_index.prompts.base import PromptTemplate
from llama_index.prompts.prompt_type import PromptType

# deprecated, kept for backward compatibility
ChoiceSelectPrompt = PromptTemplate

# DEFAULT_CHOICE_SELECT_PROMPT_TMPL = (
#     "A list of documents is shown below. Each document has a number next to it along "
#     "with a summary of the document. A question is also provided. \n"
#     "Respond with the numbers of the documents "
#     "you should consult to answer the question, in order of relevance, as well \n"
#     "as the relevance score. The relevance score is a number from 1-10 based on "
#     "how relevant you think the document is to the question.\n"
#     "Do not include any documents that are not relevant to the question. \n"
#     "Example format: \n"
#     "Document 1:\n<summary of document 1>\n\n"
#     "Document 2:\n<summary of document 2>\n\n"
#     "...\n\n"
#     "Document 10:\n<summary of document 10>\n\n"
#     "Question: <question>\n"
#     "Answer:\n"
#     "Doc: 9, Relevance: 7\n"
#     "Doc: 3, Relevance: 4\n"
#     "Doc: 7, Relevance: 3\n\n"
#     "Let's try this now: \n\n"
#     "{context_str}\n"
#     "Question: {query_str}\n"
#     "Answer:\n"
# )
DEFAULT_CHOICE_SELECT_PROMPT_TMPL = (
    "下面显示了一系列文档。每个文档旁边都有一个数字，以及文档的摘要。还提供了一个问题。\n"
    "请回复文档的数字，以回答问题，按相关性的顺序排列，同时也标注相关性得分。\n"
    "相关性得分是一个从1到10的数字，表示您认为文档与问题的相关程度。\n"
    "请不要包括与问题无关的任何文档。\n"
    "示例格式：\n"
    "文档 1：\n<文档1的摘要>\n\n"
    "文档 2：\n<文档2的摘要>\n\n"
    "...\n\n"
    "文档 10：\n<文档10的摘要>\n\n"
    "问题： <问题>\n"
    "回答：\n"
    "文档： 9，相关性： 7\n"
    "文档： 3，相关性： 4\n"
    "文档： 7，相关性： 3\n\n"
    "现在让我们试试这个：\n\n"
    "{context_str}\n"
    "问题： {query_str}\n"
    "回答：\n"
)

DEFAULT_CHOICE_SELECT_PROMPT = PromptTemplate(
    DEFAULT_CHOICE_SELECT_PROMPT_TMPL, prompt_type=PromptType.CHOICE_SELECT
)

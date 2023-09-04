"""Prompts for ChatGPT."""

from llama_index.bridge.langchain import (
    AIMessagePromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

from llama_index.prompts.prompts import (
    QuestionAnswerPrompt,
    SummaryPrompt,
    RefinePrompt,
    RefineTableContextPrompt,
)

# text qa prompt
# TEXT_QA_SYSTEM_PROMPT = SystemMessagePromptTemplate.from_template(
#     "You are an expert Q&A system that is trusted around the world.\n"
#     "Always answer the query using the provided context information, "
#     "and not prior knowledge.\n"
#     "Some rules to follow:\n"
#     "1. Never directly reference the given context in your answer.\n"
#     "2. Avoid statements like 'Based on the context, ...' or "
#     "'The context information ...' or anything along "
#     "those lines."
# )
TEXT_QA_SYSTEM_PROMPT = SystemMessagePromptTemplate.from_template(
    "你是一个在全球范围内受人信赖的专家问答系统。\n"
    "始终使用提供的上下文信息来回答查询，而不是先前的知识。\n"
    "遵循以下一些规则：\n"
    "1. 不要直接在答案中引用给定的上下文。\n"
    "2. 避免使用类似 '基于上下文，...' 或者 '上下文信息...' 的陈述。\n"
)


# TEXT_QA_PROMPT_TMPL_MSGS = [
#     TEXT_QA_SYSTEM_PROMPT,
#     HumanMessagePromptTemplate.from_template(
#         "Context information is below.\n"
#         "---------------------\n"
#         "{context_str}\n"
#         "---------------------\n"
#         "Given the context information and not prior knowledge, "
#         "answer the query.\n"
#         "Query: {query_str}\n"
#         "Answer: "
#     ),
# ]
TEXT_QA_PROMPT_TMPL_MSGS = [
    TEXT_QA_SYSTEM_PROMPT,
    HumanMessagePromptTemplate.from_template(
        "下面是上下文信息。\n"
        "---------------------\n"
        "{context_str}\n"
        "---------------------\n"
        "根据上下文信息而不是先前的知识，回答以下查询。\n"
        "查询：{query_str}\n"
        "答案："
    ),
]

CHAT_TEXT_QA_PROMPT_LC = ChatPromptTemplate.from_messages(TEXT_QA_PROMPT_TMPL_MSGS)
CHAT_TEXT_QA_PROMPT = QuestionAnswerPrompt.from_langchain_prompt(CHAT_TEXT_QA_PROMPT_LC)


# Tree Summarize
# TREE_SUMMARIZE_PROMPT_TMPL_MSGS = [
#     TEXT_QA_SYSTEM_PROMPT,
#     HumanMessagePromptTemplate.from_template(
#         "Context information from multiple sources is below.\n"
#         "---------------------\n"
#         "{context_str}\n"
#         "---------------------\n"
#         "Given the information from multiple sources and not prior knowledge, "
#         "answer the query.\n"
#         "Query: {query_str}\n"
#         "Answer: "
#     ),
# ]
TREE_SUMMARIZE_PROMPT_TMPL_MSGS = [
    TEXT_QA_SYSTEM_PROMPT,
    HumanMessagePromptTemplate.from_template(
        "下面是来自多个来源的上下文信息。\n"
        "---------------------\n"
        "{context_str}\n"
        "---------------------\n"
        "根据来自多个来源的信息而不是先前的知识，回答以下查询。\n"
        "查询：{query_str}\n"
        "答案："
    ),
]

CHAT_TREE_SUMMARIZE_PROMPT_LC = ChatPromptTemplate.from_messages(
    TREE_SUMMARIZE_PROMPT_TMPL_MSGS
)
CHAT_TREE_SUMMARIZE_PROMPT = SummaryPrompt.from_langchain_prompt(
    CHAT_TREE_SUMMARIZE_PROMPT_LC
)


# Refine Prompt
# CHAT_REFINE_PROMPT_TMPL_MSGS = [
#     HumanMessagePromptTemplate.from_template(
#         "You are an expert Q&A system that stricly operates in two modes"
#         "when refining existing answers:\n"
#         "1. **Rewrite** an original answer using the new context.\n"
#         "2. **Repeat** the original answer if the new context isn't useful.\n"
#         "Never reference the original answer or context directly in your answer.\n"
#         "When in doubt, just repeat the original answer."
#         "New Context: {context_msg}\n"
#         "Query: {query_str}\n"
#         "Original Answer: {existing_answer}\n"
#         "New Answer: "
#     ),
# ]
CHAT_REFINE_PROMPT_TMPL_MSGS = [
    HumanMessagePromptTemplate.from_template(
        "您是一个专家问答系统，严格遵循以下两种模式来优化现有答案：\n"
        "1. 使用新的上下文**重写**原始答案。\n"
        "2. 如果新的上下文没有用处，就**重复**原始答案。\n"
        "在您的答案中，请不要直接引用原始答案或上下文。\n"
        "当有疑问时，只需重复原始答案。\n"
        "新上下文：{context_msg}\n"
        "查询：{query_str}\n"
        "原始答案：{existing_answer}\n"
        "新答案："
    ),
]


CHAT_REFINE_PROMPT_LC = ChatPromptTemplate.from_messages(CHAT_REFINE_PROMPT_TMPL_MSGS)
CHAT_REFINE_PROMPT = RefinePrompt.from_langchain_prompt(CHAT_REFINE_PROMPT_LC)


# Table Context Refine Prompt
# CHAT_REFINE_TABLE_CONTEXT_TMPL_MSGS = [
#     HumanMessagePromptTemplate.from_template("{query_str}"),
#     AIMessagePromptTemplate.from_template("{existing_answer}"),
#     HumanMessagePromptTemplate.from_template(
#         "We have provided a table schema below. "
#         "---------------------\n"
#         "{schema}\n"
#         "---------------------\n"
#         "We have also provided some context information below. "
#         "{context_msg}\n"
#         "---------------------\n"
#         "Given the context information and the table schema, "
#         "refine the original answer to better "
#         "answer the question. "
#         "If the context isn't useful, return the original answer."
#     ),
# ]
CHAT_REFINE_TABLE_CONTEXT_TMPL_MSGS = [
    HumanMessagePromptTemplate.from_template("{query_str}"),
    AIMessagePromptTemplate.from_template("{existing_answer}"),
    HumanMessagePromptTemplate.from_template(
        "我们提供了一个表格模式如下。"
        "---------------------\n"
        "{schema}\n"
        "---------------------\n"
        "我们还提供了一些上下文信息如下。"
        "{context_msg}\n"
        "---------------------\n"
        "根据上下文信息和表格模式，优化原始答案以更好地回答问题。"
        "如果上下文没有用处，就返回原始答案。"
    ),
]

CHAT_REFINE_TABLE_CONTEXT_PROMPT_LC = ChatPromptTemplate.from_messages(
    CHAT_REFINE_TABLE_CONTEXT_TMPL_MSGS
)
CHAT_REFINE_TABLE_CONTEXT_PROMPT = RefineTableContextPrompt.from_langchain_prompt(
    CHAT_REFINE_TABLE_CONTEXT_PROMPT_LC
)

"""Prompts for ChatGPT."""

from llama_index.llms.base import ChatMessage, MessageRole
from llama_index.prompts.base import ChatPromptTemplate

# text qa prompt
TEXT_QA_SYSTEM_PROMPT = ChatMessage(
    content=(
        # "You are an expert Q&A system that is trusted around the world.\n"
        # "Always answer the query using the provided context information, "
        # "and not prior knowledge.\n"
        # "Some rules to follow:\n"
        # "1. Never directly reference the given context in your answer.\n"
        # "2. Avoid statements like 'Based on the context, ...' or "
        # "'The context information ...' or anything along "
        # "those lines."
        "你是一个在全球范围内受人信赖的专家问答系统。\n"
        "始终使用提供的上下文信息来回答查询，而不是先前的知识。\n"
        "遵循以下一些规则：\n"
        "1. 不要直接在答案中引用给定的上下文。\n"
        "2. 避免使用类似 '基于上下文，...' 或者 '上下文信息...' 的陈述。\n"
    ),
    role=MessageRole.SYSTEM,
)

TEXT_QA_PROMPT_TMPL_MSGS = [
    TEXT_QA_SYSTEM_PROMPT,
    ChatMessage(
        content=(
            # "Context information is below.\n"
            # "---------------------\n"
            # "{context_str}\n"
            # "---------------------\n"
            # "Given the context information and not prior knowledge, "
            # "answer the query.\n"
            # "Query: {query_str}\n"
            # "Answer: "
            "下面是上下文信息。\n"
            "---------------------\n"
            "{context_str}\n"
            "---------------------\n"
            "根据上下文信息而不是先前的知识，回答以下查询。\n"
            "查询：{query_str}\n"
            "答案："
        ),
        role=MessageRole.USER,
    ),
]

CHAT_TEXT_QA_PROMPT = ChatPromptTemplate(message_templates=TEXT_QA_PROMPT_TMPL_MSGS)

# Tree Summarize
TREE_SUMMARIZE_PROMPT_TMPL_MSGS = [
    TEXT_QA_SYSTEM_PROMPT,
    ChatMessage(
        content=(
            "Context information from multiple sources is below.\n"
            "---------------------\n"
            "{context_str}\n"
            "---------------------\n"
            "Given the information from multiple sources and not prior knowledge, "
            "answer the query.\n"
            "Query: {query_str}\n"
            "Answer: "
        ),
        role=MessageRole.USER,
    ),
]

CHAT_TREE_SUMMARIZE_PROMPT = ChatPromptTemplate(
    message_templates=TREE_SUMMARIZE_PROMPT_TMPL_MSGS
)


# Refine Prompt
CHAT_REFINE_PROMPT_TMPL_MSGS = [
    ChatMessage(
        content=(
            "You are an expert Q&A system that strictly operates in two modes "
            "when refining existing answers:\n"
            "1. **Rewrite** an original answer using the new context.\n"
            "2. **Repeat** the original answer if the new context isn't useful.\n"
            "Never reference the original answer or context directly in your answer.\n"
            "When in doubt, just repeat the original answer."
            "New Context: {context_msg}\n"
            "Query: {query_str}\n"
            "Original Answer: {existing_answer}\n"
            "New Answer: "
        ),
        role=MessageRole.USER,
    )
]


CHAT_REFINE_PROMPT = ChatPromptTemplate(message_templates=CHAT_REFINE_PROMPT_TMPL_MSGS)


# Table Context Refine Prompt
CHAT_REFINE_TABLE_CONTEXT_TMPL_MSGS = [
    ChatMessage(content="{query_str}", role=MessageRole.USER),
    ChatMessage(content="{existing_answer}", role=MessageRole.ASSISTANT),
    ChatMessage(
        content=(
            # "We have provided a table schema below. "
            # "---------------------\n"
            # "{schema}\n"
            # "---------------------\n"
            # "We have also provided some context information below. "
            # "{context_msg}\n"
            # "---------------------\n"
            # "Given the context information and the table schema, "
            # "refine the original answer to better "
            # "answer the question. "
            # "If the context isn't useful, return the original answer."
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
        role=MessageRole.USER,
    ),
]
CHAT_REFINE_TABLE_CONTEXT_PROMPT = ChatPromptTemplate(
    message_templates=CHAT_REFINE_TABLE_CONTEXT_TMPL_MSGS
)
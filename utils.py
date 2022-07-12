def print_tree(convo: Conversation, corpus: Corpus) -> None:
    """
      Prints the conversation tree with index for reference.
    """
    conv = corpus.get_conversation()
    conv.print_conversation_structure(lambda utt: str(
        utt.meta["order"])+" --- "+str(utt.speaker.id), limit=9999)



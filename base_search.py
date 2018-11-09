class BaseSearch:
    # using of the template method pattern
    def search_duplicate(self, containers):
        """
        Template method that defines sequence of actions.
        :param containers: list of containers(such as directories list).
        :return: list of duplicate items.
        """
        items = [self.get_all_items(container) for container in containers]
        dupl_items = self.do_search(items)
        return dupl_items

    def get_all_items(self, container):
        """
        Abstract method - must be implemented by subclasses.
        Searches all necessary items in the container.
        :param container: some container(such as directory).
        :return: items from container.
        """
        return NotImplementedError()

    def do_search(self, items):
        """
        Abstract method - must be implemented by subclasses.
        Searches of duplicate items.
        :param items: containers(such as python lists or dictionaries) of items.
        :return: list of duplicate items.
        """
        return NotImplementedError()

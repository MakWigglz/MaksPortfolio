class Topics_of_study:
    def __init__(self):
        self._topics = {}
        
    def add_topic(self, topic_name):
        if topic_name not in self._topics:
            self._topics[topic_name] = []
            
    def add_item(self, topic_name, *items):
        if topic_name not in self._topics:
            self.add_topic(topic_name)
        self._topics[topic_name].extend(items)
        
    def get_items(self, topic_name):
        return self._topics.get(topic_name, [])
    
    def get_all_topics(self):
        return list(self._topics.keys())
    
    def __getitem__(self, topic_name):
        return self._topics[topic_name]  
    
    def __setitem__(self, topic_name, items):
        if not isinstance(items, list) or not all(isinstance(item, str) for item in items):
            raise ValueError("Value must be a list of strings")
        self._topics[topic_name] = items
        
    def __delitem__(self, topic_name):
        del self._topics[topic_name]
        
    def __contains__(self, topic_name):
        return topic_name in self._topics 
    
    def __repr__(self):
        return f"Topics_of_study({self._topics})"
    
    def __str__(self):
        return str(self._topics)
    
    def __len__(self):
        return len(self._topics)
    
    def __iter__(self):
        return iter(self._topics)
    
topics = Topics_of_study()

topics.add_item("Science", "Physics", "Chemistry", "Biology", "Mathematics")
topics.add_item("History", "Ancient civilizations", "Modern history")

print(topics)
print(topics["Science"])
print(topics["History"])
print(len(topics))
print(list(topics))

                              
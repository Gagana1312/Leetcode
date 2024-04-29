class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails = set()
        for word in emails:
            local_word,domain_name =word.split('@')
            local_word = local_word.split('+')[0]
            local_word = local_word.replace('.','')
            word = local_word+'@'+ domain_name
            unique_emails.add(word)
        return len(unique_emails)
        
     
            
"""
Re: Fwd: Fw: Count
Given a string representing the subject line of an email, determine how many times the email has been forwarded or replied to.

For simplicity, consider an email forwarded or replied to if the string contains any of the following markers (case-insensitive):

"fw:"
"fwd:"
"re:"
Return the total number of occurrences of these markers.

1. email_chain_count("Re: Meeting Notes") should return 1.
2. email_chain_count("Meeting Notes") should return 0.
3. email_chain_count("Re: re: RE: rE: Meeting Notes") should return 4.
4. email_chain_count("Re: Fwd: Re: Fw: Re: Meeting Notes") should return 5.
5. email_chain_count("re:Ref:fw:re:review:FW:Re:fw:report:Re:FW:followup:re:summary:Fwd:Re:fw:NextStep:RE:FW:re:Project:Fwd:Re:fw:Notes:RE:re:Update:FWD:Re:fw:Summary") should return 23.
"""


def email_chain_count(subject):
    markers = ["fw:", "fwd:", "re:"]
    output = 0
    for mark in markers:
        output += subject.upper().count(mark.upper())
    return output


print(email_chain_count("re:Ref:fw:re:review:FW:Re:fw:report:Re:FW:followup:re:summary:Fwd:Re:fw:NextStep:RE:FW:re:Project:Fwd:Re:fw:Notes:RE:re:Update:FWD:Re:fw:Summary"))
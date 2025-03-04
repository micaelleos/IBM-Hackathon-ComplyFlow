import uuid

text = """12 U.S. Code § 4301 - Findings and purpose
(a)Findings
The Congress hereby finds that economic stability would be enhanced, competition between depository institutions would be improved, and the ability of the consumer to make informed decisions regarding deposit accounts, and to verify accounts, would be strengthened if there was uniformity in the disclosure of terms and conditions on which interest is paid and fees are assessed in connection with such accounts.

(b)Purpose
It is the purpose of this chapter to require the clear and uniform disclosure of—
(1)the rates of interest which are payable on deposit accounts by depository institutions; and
(2)the fees that are assessable against deposit accounts,
so that consumers can make a meaningful comparison between the competing claims of depository institutions with regard to deposit accounts.
"""

regulation = {"title":"12 U.S. Code § 4301 - Findings and purpose",
              "id":uuid.uuid4(),
              "text":text,
              "status":"Not Analized",
              "docs":[]
            }
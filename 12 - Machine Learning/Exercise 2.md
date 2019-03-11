## Exercise 2

For the following question, check the boxes that correspond to the rules that we may be able to learn. Consider the following set of 6 emails, which classify the email as spam or not. Which of the following rules might we learn? Check all that apply.

<table border="1" style="width:100%">
    <tbody><tr>
      <td style="text-align:center;vertical-align:middle">Spam or Not Spam?</td>
      <td style="text-align:center;vertical-align:middle">Spam</td>
      <td style="text-align:center;vertical-align:middle">Spam</td>
      <td style="text-align:center;vertical-align:middle">Spam</td>
      <td style="text-align:center;vertical-align:middle">Not spam</td>
      <td style="text-align:center;vertical-align:middle">Not spam</td>
      <td style="text-align:center;vertical-align:middle">Not spam</td>
    </tr>
    <tr>
      <td style="text-align:center;vertical-align:middle">Words in Email</td>
      <td style="text-align:center;vertical-align:middle">4</td>
      <td style="text-align:center;vertical-align:middle">4</td>
      <td style="text-align:center;vertical-align:middle">30</td>
      <td style="text-align:center;vertical-align:middle">35</td>
      <td style="text-align:center;vertical-align:middle">50</td>
      <td style="text-align:center;vertical-align:middle">10</td>
    </tr>
    <tr>
      <td style="text-align:center;vertical-align:middle">Flagged Words</td>
      <td style="text-align:center;vertical-align:middle">CASH, BUY, password</td>
      <td style="text-align:center;vertical-align:middle">cash, free, rolex</td>
      <td style="text-align:center;vertical-align:middle">cash free, call</td>
      <td style="text-align:center;vertical-align:middle">only, cancel, sign</td>
      <td style="text-align:center;vertical-align:middle">free, check, weight</td>
      <td style="text-align:center;vertical-align:middle">quote, cheap, website</td>
    </tr>
  </tbody></table>

- Emails containing both flagged words "cash" and "free" are marked "spam". [X]
- Emails without the flagged word "free" are marked "not spam".
- Emails with an even number of words are marked "spam".
- Emails with less than 31 words are marked "spam".
- Emails containing at least one flagged word in all capital letters are marked "spam". [X]
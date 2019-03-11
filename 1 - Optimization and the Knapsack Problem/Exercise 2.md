## Exercise 2
Please help the burglar out! For each of the following greedy metrics, what should be the burglar's first two choices of items? Here's a table of the items from the slides:

<table rules="all">
        <tbody>
          <tr>
            <td style="padding:0 5px 0 5px;">
              <b>item</b>
            </td>
            <td style="padding:0 5px 0 5px;">
              <b>$</b>
            </td>
            <td style="padding:0 5px 0 5px;">
              <b>kg</b>
            </td>
            <td style="padding:0 5px 0 5px;">
              <b>$/kg</b>
            </td>
          </tr>
          <tr></tr>
          <tr>
            <td style="padding:0 5px 0 5px;">clock</td>
            <td style="padding:0 5px 0 5px;">175</td>
            <td style="padding:0 5px 0 5px;">10</td>
            <td style="padding:0 5px 0 5px;">17.5</td>
          </tr>
          <tr>
            <td style="padding:0 5px 0 5px;">picture</td>
            <td style="padding:0 5px 0 5px;">90</td>
            <td style="padding:0 5px 0 5px;">9</td>
            <td style="padding:0 5px 0 5px;">10</td>
          </tr>
          <tr>
            <td style="padding:0 5px 0 5px;">radio</td>
            <td style="padding:0 5px 0 5px;">20</td>
            <td style="padding:0 5px 0 5px;">4</td>
            <td style="padding:0 5px 0 5px;">5</td>
          </tr>
          <tr>
            <td style="padding:0 5px 0 5px;">vase</td>
            <td style="padding:0 5px 0 5px;">50</td>
            <td style="padding:0 5px 0 5px;">2</td>
            <td style="padding:0 5px 0 5px;">25</td>
          </tr>
          <tr>
            <td style="padding:0 5px 0 5px;">book</td>
            <td style="padding:0 5px 0 5px;">10</td>
            <td style="padding:0 5px 0 5px;">1</td>
            <td style="padding:0 5px 0 5px;">10</td>
          </tr>
          <tr>
            <td style="padding:0 5px 0 5px;">computer</td>
            <td style="padding:0 5px 0 5px;">200</td>
            <td style="padding:0 5px 0 5px;">20</td>
            <td style="padding:0 5px 0 5px;">10</td>
          </tr>
        </tbody>
      </table>

For this problem, assume that the maximum weight the burglar can carry is 20.

Metric: max value
- The burglar should first pick: Computer
- and should next pick: No More Space


Metric: min weight
- The burglar should first pick: Book
- and should next pick: Vase
  
Metric: max value/weight ratio
- The burglar should first pick: Vase
- and should next pick: Clock

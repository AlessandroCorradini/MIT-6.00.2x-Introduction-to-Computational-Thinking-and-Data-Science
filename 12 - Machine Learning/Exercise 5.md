## Exercise 5

As Professor Guttag said, there are two types of people in this world: those who know programming and those who don’t. To prove this once and for all, you take a random sampling of edX students and put them through a programming test. Assume that the test is entirely fair and that it reflects the exact level of skill each student has. You also ask them to fill out a small questionnaire about their experience with 6.00.2x.

You receive the results for each student as [Exam grade, Hour spent on 6.00.2x]. That is, if Alice has spent 90 hours on 6.00.2x and received a score of 74 on the exam, you will have [74, 90] as a data point.

1. Based on your initial purposes, what should you choose as k?
- 2 [X]
- 3
- 4

2. Should you apply scaling to this data?

- Yes [X]
- No

<table>
    <tbody><tr>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">
        <b>CLUSTER 1</b>
      </td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">Exam grade</td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">Hours spent on 6.00.2x</td>
    </tr>
    <tr>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">Mean</td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">46.2</td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">4.3</td>
    </tr>
    <tr>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">Variance</td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">15.0</td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">0.91</td>
    </tr>
  </tbody></table>
  <table>
    <tbody><tr>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">
        <b>CLUSTER 2</b>
      </td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">Exam grade</td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">Hours spent on 6.00.2x</td>
    </tr>
    <tr>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">Mean</td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">84.5</td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">60.2</td>
    </tr>
    <tr>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">Variance</td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">5.1</td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">6.04</td>
    </tr>
  </tbody></table>

  Results look good – there are indeed two kinds of people, and curiously one kind seems to absolutely love 6.00.2x. However, when you rerun the code, you get the following clusters:

  <table>
    <tbody><tr>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">
        <b>CLUSTER 1</b>
      </td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">Exam grade</td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">Hours spent on 6.00.2x</td>
    </tr>
    <tr>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">Mean</td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">12.5</td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">2.34</td>
    </tr>
    <tr>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">Variance</td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">0.29</td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">0.36</td>
    </tr>
  </tbody></table>

  <table>
    <tbody><tr>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">
        <b>CLUSTER 2</b>
      </td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">Exam grade</td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">Hours spent on 6.00.2x</td>
    </tr>
    <tr>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">Mean</td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">70.23</td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">35.4</td>
    </tr>
    <tr>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">Variance</td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">8.65</td>
      <td style="border-width:1px;border-color:black;border-style:solid;padding:5px">10.84</td>
    </tr>
  </tbody></table>

  You don’t know what to believe (and, indeed, there’s no reason for you to choose one over another). What can you do to fix this and get a stable result?

- Let k = 3 [X]
- Add more students
- Add "student name length" as a feature
# [Ruby V] Escape - 9539 

[문제 링크](https://www.acmicpc.net/problem/9539) 

### 성능 요약

메모리: 385060 KB, 시간: 7948 ms

### 분류

자료 구조, 분리 집합, 그리디 알고리즘, 우선순위 큐, 작은 집합에서 큰 집합으로 합치는 테크닉, 트리

### 제출 일자

2024년 9월 13일 10:32:12

### 문제 설명

<blockquote>
<p>You hit the emperor lich with full force and slay it. There is a stair leading upwards here. You climb upstairs. You drink from the pool. You feel much better. The karmic lizard punches through your armor and hits you. You die...</p>
</blockquote>

<p>After an epic fight with the emperor lich, the hero struggles to escape the dungeon consisting of n chambers and n − 1 corridors connecting them. He starts in chamber number 1 and must reach chamber number t, moving only along the corridors. All chambers are reachable from chamber number 1. Bruised after the last fight, the hero starts the journey with 0 hit-points (HP). These points represent his health – if ever they fall below zero, the hero’s story ends there as a tragic one.</p>

<p>In some chambers there are monsters – a monster must be fought, and it always manages to take some of the hero’s HP. In some other chambers there are magic pools – every pool restores some number of the hit-points. There is no upper limit on the hero’s health. Every chamber can be visited multiple times, but the gain or loss of HP happens only once, on the very first visit.</p>

<p>Determine whether the hero can escape the dungeon alive.</p>

### 입력 

 <p>The first line of input contains the number of test cases T. The descriptions of the test cases follow:</p>

<p>The first line of each test case contains two integers: the number of chambers n, 2 ≤ n ≤ 200 000, and the number of the exit chamber t, 2 ≤ t ≤ n. The second line contains n space separated integers between -10<sup>6</sup> and 10<sup>6</sup> – the i-th of them denotes the HP gain in the i-th chamber (negative denotes a monster, positive – a pool, and zero means that the chamber is empty). The first chamber does not contain a monster, but a pool is possible there. The exit chamber may contain a pool or a monster, and the monster will have to be fought before escaping.</p>

<p>The next n−1 lines contain the descriptions of corridors. Each one contains a pair of integers – the ends of a corridor.</p>

### 출력 

 <p>For each test case print a single line containing the word escaped if escape is possible, or trapped otherwise.</p>


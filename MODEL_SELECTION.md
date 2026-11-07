# Model selection

Fill this in after you have trained your candidates in MLflow. Short sentences are fine. Use numbers from your runs.

## The question
What does this model decide, and who is hurt by a wrong answer? The model predicts if a customer will leave (churn). If it misses a customer who will leave, the company loses that customer. If it wrongly flags a loyal customer, the company wastes money on a discount.

## Candidates
| Candidate | Why I tried it | AUC | F1 | F1 per slice (lowest) | p95 latency (ms) | Size (KB) | MLflow run ID |
| logreg | simple, fast, easy to explain | 0.798 | 0.495 | 0.250 | 7.4 | 3.5 | 069459cb6cef4a84b231aac1bd50ed22 |
| random_forest | handles non-linear patterns | 0.759 | 0.454 | 0.222 | 28.6 | 3160 | 09e43002fd3d481cba0706d5e111cd5c |
| gradient_boosting | stronger tree model, often more accurate | 0.748 | 0.417 | 0.222 | 8.9 | 142 | e65fc762a42b4f939d515e0bd58585bd |

## The champion
Which one did I pick, and what decided it? (Name the numbers that mattered and the ones I accepted losing.)
I picked logreg. It has the highest AUC (0.798) and F1 (0.495), and it is also the fastest (7.4 ms) and the smallest (3.5 KB). It is best on month-to-month contracts (F1 0.543). I accepted losing on one-year contracts, where gradient_boosting is better (0.444 vs 0.250), and on two-year contracts, where random_forest is better (0.364 vs 0.250). Those slices have few customers, so the numbers are not stable.

## My promotion rules
- Latency budget (p95): 20 ms, because the service answers one customer at a time and the fastest model took 7.4 ms, so 20 ms leaves room for a slower computer in production. random_forest (28.6 ms) would be blocked.
- Minimum gain to replace the champion (F1 points): 0.01, because the test set is small and F1 changes by about 0.005 from random noise, so a smaller gain is not a real improvement.


## What I would check next
The one-year and two-year contract slices have few customers, so their F1 numbers are not stable. I would collect more data for them and check again before trusting the champion on those groups.

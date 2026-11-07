import re
p = "src/train/train_mlflow.py"
s = open(p, encoding="utf-8").read()
new = 'info = mlflow.sklearn.log_model(model, name="model", signature=signature, input_example=X_te.head(3), skops_trusted_types=["sklearn.tree._tree.Tree"])'
s2 = re.sub(r'info = mlflow\.sklearn\.log_model\(\s*\n\s*info = mlflow\.sklearn\.log_model\(.*\)\s*\n\)', new, s)
open(p, "w", encoding="utf-8").write(s2)
print("changed" if s != s2 else "no change")

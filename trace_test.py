from lean_dojo import LeanGitRepo, trace

repo = LeanGitRepo("https://github.com/zoryzhang/analogyTP_lean", "09a19fbeea480a4a704733fb1756b608cdf69285")
trace(repo, dst_dir="traced_lean4-example")
import subprocess

def run_volte_call():
    """
    Runs SIPp VoLTE call and returns True if SIP 200 OK is seen
    """

    cmd = [
        "sipp",
        "127.0.0.1",
        "-sf", "sipp/volte_call.xml",
        "-m", "1",
        "-trace_msg"
    ]

    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    output = result.stdout + result.stderr

    print("===== SIPp OUTPUT =====")
    print(output)

    if "200 <----------" in output or "200 OK" in output:
        return True

    return False


@app.route("/counters/<name>", methods=["DELETE"])
def delete_counter(name):
    """Delete a counter"""
    app.logger.info(f"Request to delete counter: {name}")

    del(COUNTERS[name])

    app.logger.info(f"Counter: {name} has been deleted")
    return '', status.HTTP_204_NO_CONTENT

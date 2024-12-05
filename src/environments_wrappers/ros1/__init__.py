
def enable_ros1(simulation_app, **kwargs) -> None:
    """
    Enables ROS1 in the simulation.

    Args:
        simulation_app (SimulationApp): SimulationApp instance.
        **kwargs: Additional keyword arguments."""

    # Enables this ROS1 extension
    from omni.isaac.core.utils.extensions import enable_extension

    enable_extension("omni.isaac.ros_bridge")
    enable_extension("omni.kit.viewport.actions")
    simulation_app.update()

    # Checks that the master is running
    import rosgraph
    import carb

    if not rosgraph.is_master_online():
        carb.log_error("Please run roscore before executing this script")
        simulation_app.close()
        exit()

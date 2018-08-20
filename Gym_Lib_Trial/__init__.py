from gym.envs.registration import register

register(
    id='tri-v0',
    entry_point='Gym_Lib_Trial.envs:TriEnv',
)
register(
    id='tri-extrahard-v0',
    entry_point='Gym_Lib_Trial.envs:TriExtraHardEnv',
)

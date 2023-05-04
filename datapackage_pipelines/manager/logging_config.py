import logging

own_name = '%-32s' % 'Main'
logging.basicConfig(
    level=logging.INFO, format=f"%(levelname)-8s:{own_name}:%(message)s"
)
logging.root.setLevel(logging.INFO)

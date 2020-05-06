from gensim.models import lda_worker
from gensim import utils
import logging
import argparse

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

parser = argparse.ArgumentParser()

parser.add_argument('-p','--port',type=int,default=9100)
parser.add_argument("--ns-host", help="Nameserver hostname (default: %(default)s)", default=None)
parser.add_argument("--ns-port", help="Nameserver port (default: %(default)s)", default=None, type=int)
parser.add_argument("--no-broadcast", help="Disable broadcast (default: %(default)s)", action='store_const',default=True, const=False)
parser.add_argument("--ns-hmac", help="Nameserver hmac key (default: %(default)s)", default=None)
parser.add_argument('--host')
parser.add_argument('-q','--quiet',action='store_const',dest="loglevel",const=logging.WARNING,default=logging.INFO)

args = parser.parse_args()

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=args.loglevel)

ns_conf = {
    "broadcast": args.no_broadcast,
    "host": args.ns_host,
    "port": args.ns_port,
    "hmac_key": args.ns_hmac
}

utils.pyro_daemon(lda_worker.LDA_WORKER_PREFIX, lda_worker.Worker(), random_suffix=True, ip=args.host,port=args.port,ns_conf=ns_conf)


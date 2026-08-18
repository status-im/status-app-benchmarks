import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from benchmark_config import BenchmarkPage  # noqa: E402

PAGE = BenchmarkPage(
    slug='wallet-fresh',
    title='New user profile',
    description='Newly created user profile',
    test_ids=(),
    user_data_size='No pre-seeded data',
    wallet_accounts='1',
    wallet_tokens='0',
    wallet_nfts='0',
    wallet_transactions='0',
    messenger_direct_chats='0',
    messenger_group_chats='0',
    communities_joined='0',
    communities_spectated='0',
)

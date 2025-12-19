#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from pathlib import Path
import argparse
import sys
import numpy as np

sns.set_theme(style="darkgrid", palette="muted")
plt.rcParams['figure.dpi'] = 200
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10

COLORS = {
    'primary': '#2E86DE',
    'success': '#10AC84',
    'warning': '#F79F1F',
    'danger': '#EE5A6F',
    'info': '#54A0FF',
    'dark': '#2C3E50'
}


def load_data(data_dir: Path) -> tuple:
    summary_file = data_dir / 'summary_metrics.csv'
    performance_file = data_dir / 'performance_metrics.csv'
    
    if not summary_file.exists():
        print(f"Error: {summary_file} not found")
        sys.exit(1)
    
    summary = pd.read_csv(summary_file)
    summary['date'] = pd.to_datetime(summary['date'])
    summary = summary.sort_values('date')
    
    performance = None
    if performance_file.exists():
        performance = pd.read_csv(performance_file)
        performance['date'] = pd.to_datetime(performance['date'])
        performance = performance.sort_values('date')
    
    return summary, performance


def plot_metric(summary: pd.DataFrame, output_dir: Path, column: str, 
                ylabel: str, title: str, filename: str, color: str,
                transform=None, target_line=None):
    fig, ax = plt.subplots(figsize=(14, 7))
    
    data = summary[column] if transform is None else transform(summary[column])
    
    ax.plot(summary['date'], data, marker='o', linewidth=3, markersize=10, 
            color=color, label=title.split()[0])
    ax.fill_between(summary['date'], 0, data, alpha=0.2, color=color)
    
    if target_line is not None:
        ax.axhline(y=target_line, color=COLORS['success'], linestyle='--', 
                  linewidth=2, alpha=0.5, label='Target')
    
    ax.set_xlabel('Date')
    ax.set_ylabel(ylabel)
    ax.set_title(title, fontweight='bold', pad=20)
    ax.legend(loc='best')
    ax.grid(True, alpha=0.4, color='#2C3E50', linewidth=0.8)
    
    unique_dates = summary['date'].dt.normalize().unique()
    ax.set_xticks(unique_dates)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    plt.tight_layout()
    plt.savefig(output_dir / filename, dpi=200, bbox_inches='tight')
    plt.close()
    print(f"Generated {filename}")


def plot_performance(performance: pd.DataFrame, test_pattern: str, 
                    title: str, filename: str, output_dir: Path):
    test_data = performance[performance['test_name'].str.contains(test_pattern, na=False)]
    
    if test_data.empty:
        print(f"Warning: No data for {test_pattern}")
        return
    
    fig, ax = plt.subplots(figsize=(14, 7))
    
    colors_list = [COLORS['success'], COLORS['primary'], COLORS['info'], COLORS['warning']]
    all_dates = []
    
    for idx, test_name in enumerate(test_data['test_name'].unique()):
        variant_data = test_data[test_data['test_name'] == test_name].copy()
        color = colors_list[idx % len(colors_list)]
        
        param_name = test_name.split('[')[1].split(']')[0] if '[' in test_name else 'default'
        
        variant_data['avg_ms'] = variant_data['avg_time'] * 1000
        variant_data['min_ms'] = variant_data['min_time'] * 1000
        variant_data['max_ms'] = variant_data['max_time'] * 1000
        
        errors = np.array([
            variant_data['avg_ms'] - variant_data['min_ms'],
            variant_data['max_ms'] - variant_data['avg_ms']
        ])
        
        ax.errorbar(variant_data['date'], variant_data['avg_ms'], yerr=errors,
                   marker='o', linewidth=3, markersize=10, label=f'{param_name} (mean)',
                   color=color, capsize=8, capthick=2, elinewidth=2, alpha=0.9)
        
        all_dates.extend(variant_data['date'].tolist())
    
    ax.set_xlabel('Date')
    ax.set_ylabel('Load Time (ms)')
    ax.set_title(title, fontweight='bold', pad=20)
    ax.legend(loc='best')
    ax.grid(True, alpha=0.4, color='#2C3E50', linewidth=0.8)
    
    unique_dates = pd.Series(all_dates).dt.normalize().unique()
    ax.set_xticks(sorted(unique_dates))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    plt.tight_layout()
    plt.savefig(output_dir / filename, dpi=200, bbox_inches='tight')
    plt.close()
    print(f"Generated {filename}")


def main():
    parser = argparse.ArgumentParser(description='Generate benchmark visualization graphs')
    parser.add_argument('--data-dir', type=Path, default=Path('data'))
    parser.add_argument('--output-dir', type=Path, default=Path('docs'))
    args = parser.parse_args()
    
    args.output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\nLoading data from {args.data_dir}...")
    summary, performance = load_data(args.data_dir)
    print(f"Loaded {len(summary)} benchmark runs")
    if performance is not None and not performance.empty:
        print(f"Loaded {len(performance)} performance results")
    
    print(f"\nGenerating graphs in {args.output_dir}...")
    
    plot_metric(summary, args.output_dir, 'pass_rate', 'Pass Rate (%)', 
                'Pass Rate Trend', 'pass_rate_trend.png', COLORS['primary'], target_line=100)
    plot_metric(summary, args.output_dir, 'total_duration_ms', 'Duration (minutes)',
                'Total Test Suite Duration', 'total_duration.png', COLORS['info'],
                transform=lambda x: x / 1000 / 60)
    plot_metric(summary, args.output_dir, 'total_retries', 'Retry Count',
                'Test Retries Over Time', 'retry_count.png', COLORS['warning'])
    plot_metric(summary, args.output_dir, 'flaky_tests', 'Flaky Test Count',
                'Flaky Tests Over Time', 'flaky_tests.png', COLORS['danger'])
    
    if performance is not None and not performance.empty:
        print("\nGenerating performance metrics...")
        plot_performance(performance, 'test_wallet_loading_time',
                        'Wallet Screen Loading Time Performance',
                        'wallet_loading_time.png', args.output_dir)
        plot_performance(performance, 'test_swap_loading_time',
                        'Swap Screen Loading Time Performance',
                        'swap_loading_time.png', args.output_dir)
    
    print(f"\nAll graphs generated in {args.output_dir.absolute()}")


if __name__ == '__main__':
    main()
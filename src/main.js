const chalk = require('chalk');
const { program } = require('commander');

program
  .option('-i, --interface <interface>', 'network interface to capture on')
  .option('-f, --filter <filter>', 'packet filter expression')
  .parse(process.argv);

const options = program.opts();

console.log(chalk.red('Error: Network packet capture is not supported in this environment.'));
console.log(chalk.yellow('This feature requires native system access that is not available in WebContainer.'));
console.log(chalk.yellow('Please run this application in a native Node.js environment instead.'));

process.exit(1);
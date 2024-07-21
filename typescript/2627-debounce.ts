type F = (...args: number[]) => void;

function debounce(fn: F, t: number): F {
  let timeout: any = null; // lol any
  return function (...args) {
    if (timeout) {
      clearTimeout(timeout);
    }

    timeout = setTimeout(() => fn(...args), t);
  };
}

const log = debounce(console.log, 5000);

log(123); // after 5000ms: 123

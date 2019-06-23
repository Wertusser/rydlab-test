const frequency = array => {
    const freq = {};
    array.forEach(item => {
        freq[item] = freq[item] || 0;
        freq[item]++;
    });
    return Object.getOwnPropertyNames(freq)
        .map(key => [key, freq[key]]);
};

const pronounceFile = amount => {
    return amount > 1 ? "files" : "file"
};

const handleEditor = (filenames, editors) => {
  return  [...filenames].map((item, i) => {
      return {filename: item.value, text: editors[i].value}
  });
};

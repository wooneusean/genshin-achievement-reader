// Load json from completed.json
var open = indexedDB.open('paimonmoe');
open.onerror = function (event) {
  console.log('Error loading database');
};
open.onsuccess = function (event) {
  var db = open.result;
  var transaction = db.transaction('keyvaluepairs', 'readwrite');
  var objectStore = transaction.objectStore('keyvaluepairs');
  objectStore.put(
    /* Paste the contents of `completed.json` here */,
    'achievement'
  );
  console.log('Success!');
};

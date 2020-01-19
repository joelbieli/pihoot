/**
 * File description:
 * Contains utility files that are used globally.
 */

/**
 * Returns a clone of the object passed in.
 *
 * This functionality is crucial when wanting to compare edited quizzes to what was in the database when it was last
 * updated. Since javascript is pass-by-reference if I were to update one of the objects that were previously assigned
 * to one another, the value would change for both of them.
 *
 * @global
 *
 * @param {Object} obj The object to clone.
 *
 * @return {Object} The cloned object
 */
export const passByVal = (obj) => JSON.parse(JSON.stringify(obj));
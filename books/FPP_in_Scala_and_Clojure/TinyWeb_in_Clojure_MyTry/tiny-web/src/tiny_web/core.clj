(ns tiny-web.core  
  (:gen-class)
  (:import (tinyweb HttpRequest HttpRequest$Builder))
  (:import (tinyweb RenderingException))
  (:import (other Test01))
  (:import (other Test03))
  )

(require '[tiny-web.view :as view])
(require '[tiny-web.tw :as tw])
(require '[tiny-web.request :as hreq])

;; step1

;(defn test-controller [http-request] {:name (.getBody http-request)})
(def t01 (new Test01 "my-name-of-test01"))
(println "name = " (.get t01))
(def t03 (new Test03 "my-name-of-test03"))
(println "name3 = " (.get t03))

(def test-builder (HttpRequest$Builder/newBuilder))
(def test-http-request  (.. test-builder (body "Mike") (path "/say-hello") build))
(def test-http-request-map {:body "Mike" :path "/say-hello" :headers {}})
;(defn test-controller-with-map [http-request] {:name (http-request :body)})

;; step2

(defn test-controller [http-request] {:name (http-request :body)})
(defn test-view [model]
  (str "<h1>Hello, " (model :name) "</h1>"))
(defn- render [view model]
  (try
    (view model)
    (catch Exception e (throw (RenderingException. e)))))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println "body = " (.getBody test-http-request))
  

)

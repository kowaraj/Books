(ns tiny-web.core  
  (:gen-class)
  (:import (tinyweb HttpRequest HttpRequest$Builder))
  (:import (tinyweb RenderingException))
  )

(require '[tiny-web.view :as view])
(require '[tiny-web.tw :as tw])
(require '[tiny-web.request :as hreq])

;; step1

;(defn test-controller [http-request] {:name (.getBody http-request)})
(def test-builder (HttpRequest$Builder/newBuilder))
(def test-http-request  (.. test-builder (body "Mike") (path "/say-hello") build))
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
